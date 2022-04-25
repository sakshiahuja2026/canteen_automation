from venv import create
from django.urls import include, path
from django.contrib import admin
from .views import AddToCartView, AddressView, CartListView, SingleProductView, createfood,viewfood
from a_food import views

urlpatterns = [
     path('add/', createfood.as_view(),name = 'menu'),
     path('',views.index),
     path('view/',viewfood.as_view(),name='viewall'),
     path ('add/',createfood.as_view()),
     path('add_to_cart/',AddToCartView.as_view(),name='add_to_cart'),
     path('cart/',CartListView.as_view(),name='cart'),
      path('checkout/',views.CheckoutView.as_view(),name='checkout'),
    path('checkout-1/',AddressView.as_view(), name='address'),
    path('single_product/<pk>', SingleProductView.as_view(),name='single_product'),
     


]   