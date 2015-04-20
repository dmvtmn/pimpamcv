from django.db import models
from ppcv.models import Service
# Create your models here.

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
