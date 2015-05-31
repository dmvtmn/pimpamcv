from django.db import models
#from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from django.conf import settings
from ppcv.models import Service
# Create your models here.

#User = get_user_model() having error on this - lecture "update order model"

class Cart(models.Model):
    service = models.ForeignKey(Service, null=True, blank=True) #might want the cart to exist, although not have service in the cart
    coupon = models.ForeignKey('Coupon', null=True, blank=True)
    total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    active= models.BooleanField(default=True)

    def __unicode__(self):
        return "Cart id: %s" %(self.id)
'''
    def get_total(self, discount=None):
        total = (self.service).price
        if discount:
            new_total = total - (total*discount)
            total=new_total
        return total
'''

STATUS_CHOICES= (
        ("Started", "Activo"),
        ("Cancelled", "Cancelado"),
        ("Finished", "Terminado"),
)

class Order(models.Model):
    #add sub total tax, final price in the future
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank = True, null= True)
    order_id = models.CharField(max_length=120, default= "ABC", unique=True) #want unique orders
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120, choices = STATUS_CHOICES, default= "Started")
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.order_id)


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=6, unique=True)
    description = models.CharField(max_length=120, null=True, blank= True)
    discount_value= models.DecimalField(max_digits=100, decimal_places=2,default=0.25)
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    active= models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.coupon_code)

'''
Add stripe coupon
'''
