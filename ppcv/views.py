from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, UsrDoc
# Create your views here.

def usr_home(request):
    return render(request, 'ppcv/usr_home.html', locals())
