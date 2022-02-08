from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product

class Cart(View):
    def get(self, request):
        if not request.session.get('cart'):
            return render(request, 'emptycart.html')
        else:
            ids = list(request.session.get('cart').keys())
        # ids = list(request.session.cart.keys())
        products = Product.get_products_by_id(ids)
        # print(products)
        # print(list(request.session.get('cart').keys()))
        # print(type(list(request.session.get('cart').keys())))
        return render(request, 'cart.html', {'products' : products})

