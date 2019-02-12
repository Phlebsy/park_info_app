# Park Announcement App

This application queries and stores announcements made by the National Park Service. To interact with the application:

1: Choose a Park code from the list here: https://nps-vsp.warnercnr.colostate.edu/showallparkunits.php

2: Input the code on the form while on the localhost:8000 page and click "Add Code"

3: The announcements(if any) will be queried, saved, and displayed. To view all the announcements currently in the database from here, click "View All Announcements"

On the View All Announcements page you can click on individual park codes on the right-most column to find announcements for that park only, add another code, or clear the database.

## Requirements

Python3 and virtualenv are required to run this project. All other dependencies are installed via pip in the virtual environment.

## Starting the project:

Setup and activate a virtual environment:

`python3 -m virtualenv env`

`source env/bin/activate`

You should see a (env) to the left of your command line directory - this indicates that it was successful.

Next, navigate to the root directory of this project then run:

`pip install -r requirements.txt`

Finally, start the server and navigate to localhost:8000 in a web browser:

`python manage.py runserver`

## Database:

This project makes use of a managed PostgreSQL database via ElephantSql. To use a local one you will need to change the NAME, USER, PASSWORD, HOST and PORT fields under DATABASES in park_info_app/settings.py to point to your own, 
