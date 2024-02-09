Welcome to Patricks Posting Forum

Basic information about the project

- Core FrameWork is Django 4.2 and Up
- Using Python 3.9
- Django Rest Framework 2.14.0
- Application built on Windows Environment (but platform agnostic)

To begin the project:
- Create an appropriate venv to store the projects dependencies
- python -m venv /path/to/new/virtual/environment
- make sure the environment is active: source env/bin/activate
- Head to the root folder and install dependencies: pip install -r .\requirements.txt

To run the application, 
 [venv_location]\Scripts\python.exe manage.py runserver 8000 


Project Structure

PattysForum
-> ai 
  -> views.py
   -> Analytics => code for the our post prediction engine
-> api
   -> serializers.py
   -> views.py
   -> urls.py
-> comment (Application for managing Comments)
-> common
  -> views.py
   -> Metrics => code to measure frequency of produced posts /day and per hour for each our over the last 24 hours   
-> like (Application for managing Likes)
-> post (Application for managing Posts)
-> pattysForum (Core Application which hosts configs, settings)

Docmentation Folder
- Postman Collection
- Document Overview
- Project Diagram