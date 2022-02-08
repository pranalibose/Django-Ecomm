from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')
        phone = postData.get('phone')
        conpass = postData.get('conpass')

        # fetch values
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        # validate
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password,
                            conpass=conpass)

        error_message = self.validate(customer)

        # save
        if not error_message:
            customer.password = make_password(customer.password)
            customer.conpass = make_password(customer.conpass)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validate(self, customer):
        error_message = None

        if not customer.first_name:
            error_message = 'First name is Required!'
        elif len(customer.first_name) < 3:
            error_message = 'First name should atleast be 3 characters long!'
        elif not customer.last_name:
            error_message = 'Last name is Required!'
        elif len(customer.last_name) < 3:
            error_message = 'Last name should atleast be 3 characters long!'
        elif not customer.phone:
            error_message = 'Phone Number is Required!'
        elif len(customer.phone) != 10:
            error_message = 'Phone should be 10 digits long!'
        elif not customer.email:
            error_message = 'Email is Required!'
        elif not customer.password:
            error_message = 'Password is Required!'
        elif len(customer.password) < 6:
            error_message = 'Password should atleast be 6 characters long!'
        elif customer.password != customer.conpass:
            error_message = 'Password mismatch!'
        elif customer.isExists() == True:
            error_message = 'Email already exists!'

        return error_message