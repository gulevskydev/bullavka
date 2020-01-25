from django.shortcuts import render
from main.models import Logo
# Create your views here.

def cooperation(request):
    logo = Logo.objects.latest('pk')
    return render(request, 'cooperation/cooperation.html', context={'logo': logo})