from django.contrib import admin
from .models import *



class CoffeehouseAdmin(admin.ModelAdmin):
   list_display = [field.name for field in Coffeehouse._meta.fields]

   class Meta:
       model = Coffeehouse

admin.site.register(Coffeehouse, CoffeehouseAdmin)


class JobNameAdmin(admin.ModelAdmin):
   list_display = [field.name for field in JobName._meta.fields]

   class Meta:
       model = JobName

admin.site.register(JobName, JobNameAdmin)


class JobAdmin (admin.ModelAdmin):
   list_display = [field.name for field in Job._meta.fields]

   class Meta:
       model = Job

admin.site.register(Job, JobAdmin)