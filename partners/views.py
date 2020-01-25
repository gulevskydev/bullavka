from django.shortcuts import render
from main.models import Logo
from .models import Partners
# Create your views here.

def partners(request):
    logo = Logo.objects.latest('pk')
    partners = Partners.objects.all()
    return render(request, 'partners/partners.html', context={'logo': logo,
                                                              'partners': partners})