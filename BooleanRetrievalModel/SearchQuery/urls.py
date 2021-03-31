from django.contrib import admin
from django.urls import path
from SearchQuery import views

from django.conf.urls import url

urlpatterns = [
    url('', views.renderHome, name='home'),
   
    
]