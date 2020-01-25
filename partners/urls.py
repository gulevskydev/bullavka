from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', partners, name='partners_url'),
]