from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
   path('', Jobs.as_view(), name='jobs_url'),
   path('form', JobFormModel.as_view(), name='form_url'),
   path('ajax/load-jobnames/', load_jobnames, name='ajax_load_jobnames'),
   path('ajax/load-jobnames-jobs/', load_jobnames_jobs, name='ajax_load_jobnames_jobs'),
]
