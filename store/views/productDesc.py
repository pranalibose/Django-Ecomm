from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product

class Description(View):
    def get(self, request):
        id = request.session.get('product')
        print(id)
        product = Product.objects.get(id=1)
        # return redirect('homepage')
        return render(request, 'proddesc.html', {'products' : product})
#
