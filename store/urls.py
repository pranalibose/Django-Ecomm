from django.urls import path

from .views import home, login, signup
from .views.aboutus import AboutUs
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.contactus import ContactUs
from .views.login import logout
from .views.orders import OrderView
from .views.productDesc import Description

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home.Index.as_view(), name = 'homepage'),
    path('signup', signup.Signup.as_view(), name= 'signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('proddesc', Description.as_view(), name='proddesc'),
    path('checkout', CheckOut.as_view(), name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),
    path('contactus', ContactUs.as_view(), name='contactus'),
    path('aboutus', AboutUs.as_view(), name='aboutus'),


#     Password Reset URLs
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')
]
