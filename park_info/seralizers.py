from rest_framework import serializers
from .models import ParkInfo


class ParkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkInfo
        fields = ('title', 'id', 'description', 'category', 'url', 'parkCode')

        def __str__(self):
            return self.title
