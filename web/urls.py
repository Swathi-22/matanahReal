from unicodedata import name
from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('product/', views.product,name='product'),
    path('gallery/', views.gallery,name='gallery'),
    path('contact/', views.contact,name='contact'),
]