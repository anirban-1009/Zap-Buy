from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import Product
from cart.cart import Cart

@login_required
def home(request):
    items = Product.objects.all()
    return render(request, 'marketplace/home.html', {'items': items})

# @login_required
# def buy_item(request, id):
#     current_user = request.user.id
#     try:
#         cart = CartItem.objects.get()
        
#     except Cart.DoesNotExist:
#         print("User Not found")
    
#     return redirect('home')


@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'marketplace/cart_detail.html')