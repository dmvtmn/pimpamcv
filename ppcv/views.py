from django.shortcuts import render, Http404
from django.http import HttpResponse
from .models import Category, Service
# Create your views here.

def usr_home(request):
    return render(request, 'ppcv/usr_home.html', locals())

#create view of single service

def single(request, slug):
    try:
        service = Service.objects.get(slug=slug)
        context = {'service': service}
        template = 'ppcv/service.html'
        return render(request, template, context)
    except Service.DoesNotExist:
        raise Http404
