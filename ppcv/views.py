from django.shortcuts import render, Http404
from django.http import HttpResponse
from .models import Category, Service, UsrDoc, Revision, Post
# Create your views here.

def usr_home(request):

    revisions = Revision.objects.all()
    revision_posts = Post.objects.all()
    user_docs = UsrDoc.objects.all()
    context = {'user_docs': user_docs, 'revisions': revisions, 'revision_posts': revision_posts }
    return render(request, 'ppcv/usr_home.html', context )

#create view of single service

def single(request, slug):
    try:
        service = Service.objects.get(slug=slug)
        other_services = Service.objects.all().exclude(slug=slug)
        #images = ServiceImage.objects.filter(service=service)
        context = {'service': service, 'other_services': other_services}
        template = 'ppcv/service.html'
        return render(request, template, context)
    except Service.DoesNotExist:
        raise Http404
