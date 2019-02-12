from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import ParkInfo
from .seralizers import ParkInfoSerializer
from .utils import check_park_code
import requests
import json


class ParkInfoView(viewsets.ModelViewSet):
    queryset = ParkInfo.objects.all()
    serializer_class = ParkInfoSerializer

# auth is out of scope for this project so secure connection requirement is disabled for POST request
@csrf_exempt
def addCode(request):
    # Parse body

    if(request.method == 'GET'):
        return render(request, 'parks/addCode.html')
    else:
        input_park_code = request.POST['parkCode']

        # Used for non-form based HTTP requests
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # input_park_code = body['parkcode']

        # Check for valid input, reject request if invalid
        if check_park_code(input_park_code) is False:
            return render(request, 'parks/addCode.html', {'message': 'Please input a valid park code from the NPS Park Unit Abbreviations.'})

        # Query external API for park announcements and parse the JSON data
        url = 'https://developer.nps.gov/api/v1/alerts?parkCode={0}&api_key=LMFTFw19RWucNqzFNUjEnsWyALY8SBmTsCeMBb6Z'.format(
            input_park_code)
        query_result = requests.get(url)
        info_list = query_result.json()['data']

        # Stop execution if no results from API
        if len(info_list) == 0:
            return render(request, 'parks/addCode.html', {'message': 'No announcements for Park code {0}'.format(input_park_code)})

        # Remove old announcements for this code from the database
        ParkInfo.objects.filter(parkcode=input_park_code).delete()

        # raw removal query, doesn't work due to not waiting for the database to finish executing the query before moving on
        # ParkInfo.objects.raw(
        #     'DELETE FROM park_info_parkinfo WHERE parkcode = \'{0}\''.format(input_park_code))

        # Build array of records to save
        park_announcements = []
        for record in info_list:
            park_announcements.append(ParkInfo(
                title=record['title'],
                id=record['id'],
                description=record['description'],
                category=record['category'],
                url=record['url'],
                parkcode=record['parkCode']))

        # Save to database
        ParkInfo.objects.bulk_create(park_announcements)

        return redirect('viewCode/{0}'.format(input_park_code))


def index(request):
    print('in index')

    return render(request, 'index.html', {
        'foo': 'bar',
    })
    # template = loader.get_template('index.html')
    # context = {}
    # return HttpResponse(template.render(context, request))


def viewAll(request):
    # Retrieve records from database
    values = ParkInfo.objects.values()

    # Convert from ParkInfo list to dict list
    park_announcements = [entry for entry in values]

    return render(request, 'parks/viewAll.html', {
        'park_announcements': park_announcements,
        'num_announcements': len(park_announcements)
    })


def viewCode(request, parkcode):
    # Retrieve records for this code from database
    values = ParkInfo.objects.filter(parkcode=parkcode)

    # Convert from ParkInfo list to dict list
    park_announcements = [entry for entry in values]

    return render(request, 'parks/viewCode.html', {
        'parkcode': parkcode,
        'park_announcements': park_announcements,
        'num_announcements': len(park_announcements)
    })


def clearData(request):
    ParkInfo.objects.all().delete()
    return redirect('addCode')
