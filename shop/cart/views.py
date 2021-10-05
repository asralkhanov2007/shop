from django.shortcuts import render,redirect
from .models import *
from main.models import Product
from django.http import JsonResponse, HttpResponse
from .forms import AddOrderForm

# Create your views here.
def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create()
        request.session['user_cart_id'] = cart.id
    return cart



def cartView(request):
    return render(request, 'cart.html')

import json
def addToCart(request):
    d = request.GET.get('data')
    data  = json.loads(d)
    print(data)
    product_id = data['product_id']
    quantity = data['count']
    cart = cart_init(request)
    cart.add(product_id,quantity)
    status = {

    }
    if cart:
        status['success'] = 200
    else:
        status['error'] = 400
    return JsonResponse(status)

def deleteCartItem(request,product_id,qty):
    cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    cart.deleteItem(product_id,qty)
    return redirect('cart:cart')

def removeCart(request):
    print(request.path)
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        return redirect('main:home')
    cart.delete()
    return redirect('main:home')

def addOrder(request,cart_id):
    cart = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
           order =  form.save()
           for p in cart.products.all():
               order.products.create(
                   product=p.product,
                   quantity=p.quantity,
                   price=p.quantity * p.price
               )
           order.payed = False
           order.save()
           last_order = Order.objects.last()
           return render(request, 'order_done.html', {'order': last_order})
    else:
        form = AddOrderForm()
    # pass
    return render(request,'order.html',{'form':form} )