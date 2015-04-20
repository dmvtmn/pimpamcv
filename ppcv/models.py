from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from os.path import basename

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class UsrDoc(models.Model):
    category = models.ForeignKey(Category, related_name='type', default=1, null=False, blank=True)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name='owner', default=1, null=False, blank=True)
    attachment = models.FileField(upload_to='attachments', null=True, blank=True)
    description = models.TextField(null=True)
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)
    active= models.BooleanField(default=True)

    def __unicode__(self):
        return basename(self.attachment.name)

class Service(models.Model):
    title = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=29.99)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)
    active= models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.title)

class ServiceImage(models.Model):
    service = models.OneToOneField(Service, primary_key=True)
    image = models.FileField(upload_to='services/images/', null=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active= models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)

    def __unicode__(self):
        return str(self.service.title)

class Revision(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=2000, null=False, blank=False)
    service = models.ForeignKey(Service,related_name='revision', default=1, null=False, blank=True)
    created =  models.DateTimeField(auto_now=False, auto_now_add=True, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True)
    user = models.ForeignKey(User, related_name='lister', default=1, null=False, blank=True)
    rating = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class Post(models.Model):
    revision=models.ForeignKey(Revision)
    poster = models.ForeignKey(User, related_name='poster', default=1, null=False, blank=True)
    content=models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True)

    def __unicode__(self):
        return self.content
