# chat
There is a simple chat example, realised via Django, django-channels and React.

To run locally:
- pip install -r requirements.txt
- python manage.py migrate
- daphne chat.asgi:channel_layer --port 8000
- python manage.py runworker
