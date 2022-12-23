
from django.contrib import admin
from django.urls import path 
from .views import CountryListView , CountryDetailView
urlpatterns = [
    path('' , CountryListView.as_view() , name="list"  ),
    path('<int:pk>' , CountryDetailView.as_view() , name="detail"   ),
]

