from django.shortcuts import render, redirect
from django.template.context_processors import request

from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product

class ContactUs(View):
    def get(self, request):
        return render(request, 'contaactus.html')

