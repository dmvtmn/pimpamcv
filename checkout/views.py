import time
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from ppcv.models import Service
from .models import Cart, Order
from .utils import id_generator

# Create your views here.

def view(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None

    if the_id:

        context = {"cart": cart}
    else:
        empty_message = "Tu carrito esta vacio"
        context = {"empty": True, "empty_message": empty_message }

    template= "checkout/view.html"
    return render(request,template,context)

"""
def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("cart"))
    cart
Consider need to this view

"""

def update_cart(request, slug):
    request.session.set_expiry(36000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id']=new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        service = Service.objects.get(slug=slug)
    except Service.DoesNotExist:
        pass
    except:
        pass
    new_total = 0.00
    if not cart.service:
        cart.service = service
        new_total += float(cart.service.get_price())
    else:
        cart.service= None

    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse("cart"))

def orders(request):

    context = {}
    template = "checkout/user.html"
    return render(request, template, context)

#require user login
@login_required
def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        #work on some error message
        return HttpResponseRedirect(reverse("cart"))


    #new_order,created = Order.objects.get_or_create(cart=cart) get or create actually saves it

    # run credit card
    if new_order.status == "Finished":
        del request.session['cart_id']
        #del request.session['items_total']
        # cart.delete() if wanted to delete cart
        return HttpResponseRedirect(reverse("cart"))

    context = {}
    template = "index.html"
    return render(request, template, context)
