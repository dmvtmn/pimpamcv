from django.contrib import admin
from .models import Cart,Coupon


# Register your models here.

class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart

class CouponAdmin(admin.ModelAdmin):
    class Meta:
        model = Coupon

admin.site.register(Cart, CartAdmin)
admin.site.register(Coupon, CouponAdmin)
