from django.shortcuts import render
from django.http import HttpResponse
from ppcv.models import Service, UsrDoc

# Create your views here.

def index(request):
    if request.user.is_authenticated():
        usrdoc_list = UsrDoc.objects.all()
        context_dict = {'usrdocs':usrdoc_list}
        template = 'ppcv/usr_home.html'
    else:
        service_list = Service.objects.all()
        context_dict = {'services':service_list}
        template = 'index.html'

    return render(request, template , context_dict)
