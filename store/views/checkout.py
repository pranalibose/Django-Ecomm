from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            order = Order(product=product,
                          customer=Customer(id=customer),
                          quantity=cart.get(str(product.id)),
                          price=product.price,
                          address=address,
                          phone=phone
                          )
            # order.placeOrder()
            print(order.save())
        request.session['cart'] = {}
        return redirect('cart')
