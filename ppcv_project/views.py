from django.shortcuts import render
from django.http import HttpResponse
from ppcv.models import Service, UsrDoc

# Create your views here.

def index(request):
    service_list = Service.objects.all()
    context_dict = {'services':service_list}
    return render(request, 'index.html', context_dict)
