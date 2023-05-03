from django.shortcuts import render, redirect
from .models import Car, Cart, HomeInfo
# Create your views here.


def home(request):
    cart_list = Cart.objects.all()
    home_info = HomeInfo.objects.all()[0]
    return render(request, 'main/home.html', context={
        'cart_list':cart_list,
        'home_info':home_info

    })


def product(request):
    car_list = Car.objects.all()
    cart_list = Cart.objects.all()

    return render(request, 'main/product.html', context={
        'car_list':car_list,
        'cart_list':cart_list

    })


def cart(request):
    summ = 0
    if request.method == 'POST':
        car_id = request.POST.get('id')
        my_car = Car.objects.get(id=car_id)
        Cart.objects.create(car=my_car)
        return redirect('product')
    cart_list = Cart.objects.all()
    for i in cart_list:
        summ += i.car.price
    return render(request, 'main/cart.html', context={
        'cart_list':cart_list,
        'summ':summ
    })


def delete_car(request):
    if request.method == 'POST':
        car_id = request.POST.get('id')
        Cart.objects.filter(id=car_id).delete()
        return redirect('cart')