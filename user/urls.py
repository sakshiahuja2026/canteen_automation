from venv import create
from django.urls import include, path
from django.contrib import admin
from user import views
from .views import createreservation,viewreservation,detailreservation,deletereservation,updatereservation,createcontact,viewcontact,deletecontact,updatecontact,detailcontact
urlpatterns = [
    
     path('',views.index),
     path('createreservation/',createreservation.as_view(),name='reservationbook'),
     path ('viewreservation/',viewreservation.as_view(),name='viewreservation'),
     path ('detailreservation/<int:pk>',detailreservation.as_view(),name='detail'),
     path ('deletereservation/<int:pk>',deletereservation.as_view(),name='delete'),
     path ('updatereservation/<int:pk>',updatereservation.as_view(),name='update'),
     path ('createcontact/',createcontact.as_view(),name = "createcontactus"),
     path ('viewcontact/',viewcontact.as_view(),name='viewcontack'),
     path ('detailcontact/<int:pk>',detailcontact.as_view(),name='detail'),
     path ('deletecontact/<int:pk>',deletecontact.as_view(),name='delete'),
     path ('updatecontact/<int:pk>',updatecontact.as_view(),name='update'),
     
     


]   