from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        print(product)
        remove = request.POST.get('remove')
        print(remove)
        cart = request.session.get('cart')
        print(cart)
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')


    def get(self, request):
        products = None
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        # request.session.get('cart').clear()
        # return  render(request , 'orders/order.html')
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_id(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        # print('You are = ', request.session.get('email'))
        return render(request, 'index.html', data)



