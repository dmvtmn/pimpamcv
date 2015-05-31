from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.db import models
from os.path import basename

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class UsrDoc(models.Model):
    category = models.ForeignKey(Category, related_name='type',verbose_name="Tipo de documento",\
                                                                default=1, null=False, blank=True)
    title = models.CharField(max_length=128)
    #views = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name='autor', default=1, null=False, blank=True)
    attachment = models.FileField(upload_to='attachments', null=True, blank=True)
    description = models.TextField(null=True)
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True) #added to DB
    updated=models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True) # last updated
    active= models.BooleanField(default=True)

    def __unicode__(self):
        return basename(self.attachment.name)

class Service(models.Model):
    title = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=29.99)
    description = models.CharField(max_length=2000, null=True, blank=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    slug = models.SlugField(unique=True)# unique clause so that you have unique services
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)
    active= models.BooleanField(default=True)

    #need to add method get_price()

    class Meta:
        unique_together = ('title', 'slug') #title and slug unique together

    def get_price(self):
        return self.price

    def __unicode__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("single_service", kwargs={"slug": self.slug})

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
    service = models.OneToOneField(Service, related_name='revision')
    indoc = models.ForeignKey(UsrDoc,related_name='doc inicial', default=1, null=True, blank=True)
    outdoc = models.ForeignKey(UsrDoc,related_name='doc final', default=1, null=True, blank=True)
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
