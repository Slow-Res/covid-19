
from django.contrib import admin
from django.urls import path 
from .views import Home , Country , All_Countries
urlpatterns = [
    path('' , Home , name='home' ),
    path('date/' , Country , name='country' ),
    path('all/' , All_Countries , name='all' ),
]


