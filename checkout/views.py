from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Cart
from ppcv.models import Service

# Create your views here.

def view(request):
    cart = Cart.objects.all()[0]
    context = {"cart": cart}
    template= "checkout/view.html"
    return render(request,template,context)

def update_cart(request, slug):
    cart = Cart.objects.all()[0]
    try:
        service = Service.objects.get(slug=slug)
    except Service.DoesNotExist:
        pass
    except:
        pass
    if not cart.service:
        cart.service = service
    else:
        cart.service.delete()
    return HttpResponseRedirect(reverse("cart"))
