from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('', views.index ,name='home'),
    path('home/', views.index ,name='home'),
    path('service/', views.service ,name='service/'),
    path('about/', views.about ,name='about/'),
    path('djcon/', views.djcon ,name='jd/'),
    path('jdcon/', views.jdcon ,name='dj/'),
    path('addContact/', views.addContact ,name='addContact/'),
]
