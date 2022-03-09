from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"), 
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    
]
