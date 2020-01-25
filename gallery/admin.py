from django.contrib import admin
from .models import *



class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

class InteriorInline(admin.TabularInline):
    model = Interior
    extra = 0

class BeverageInline(admin.TabularInline):
    model = Beverage
    extra = 0

# Register your models here.
class GalleryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Gallery._meta.fields]
    inlines = [ProductInline, InteriorInline, BeverageInline]

    class Meta:
        model = Gallery

admin.site.register(Gallery, GalleryAdmin)
