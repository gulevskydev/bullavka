from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Contacts.as_view(), name='contacts_url'),
]