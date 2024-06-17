from django.contrib import admin
from .models import Profile
from .models import Notification

""" 
    Concluding on the most recent actualization of Django, 
    this creates the user model instantly when we run the command 
    python manage.py to anyway app and else the register it.
"""

admin.site.register(Profile)
admin.site.register(Notification)
