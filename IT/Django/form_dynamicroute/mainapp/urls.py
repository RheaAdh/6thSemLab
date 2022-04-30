from django.conf.urls import url,include
from . import views
from django.urls import path

urlpatterns=[
    url('login/',views.login),
    url('dashboard/',views.dashboard),
    path('<int:x_num>/',views.x)
]