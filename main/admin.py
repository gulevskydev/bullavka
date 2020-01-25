from django.contrib import admin
from .models import *

admin.site.register(Logo)

class VideosInline(admin.TabularInline):
    model = Videos
    extra = 0

class PhotosInline(admin.TabularInline):
    model = Photos
    extra = 0

# Register your models here.
class VPAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Video_or_Photo._meta.fields]
    inlines = [VideosInline, PhotosInline]

    class Meta:
        model = Video_or_Photo

admin.site.register(Video_or_Photo, VPAdmin)
