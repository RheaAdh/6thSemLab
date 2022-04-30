from django.conf.urls import url
from . import views

urlpatterns = [
#  url(r'^connection/',views.formView, name = 'formView'),
 url('login', views.login, name = 'login'),
 url('logout', views.logout, name = 'logout'),
 url('cart',views.cart,name="cart"),
 url('register',views.register,name="register"),
 url('',views.index,name='index')
]