"""foodempire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
import UserApp
from user.views import createcontact, index,menu,reservation1,contact,about,gallery,stuff,blog,blog_single,normalindex
from user.views import createreservation,reservation1,contact1,createcontact,viewreservation,detailreservation,deletereservation,updatereservation,viewcontact,detailcontact,deletecontact,updatecontact
from a_food.views import createfood
from django.contrib.auth.views import LoginView, LogoutView
from UserApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('normalindex/',normalindex,name='normalindex'),
    path('a_food/view/normalindex/',normalindex,name='normalindex'),
    path("a_food/",include("a_food.urls")),
    path("userapp/",include("UserApp.urls")),
    path('index/',index,name='index'),
    path('menu/',menu,name='menu'),
    path('reservation/',reservation1,name='reservation'),
    path('rev/',createreservation.as_view(),name='createreservation'),
    path('cont/',createcontact.as_view(),name='createcontact'),
    path('contact/',contact1,name='contact'),
    path('about/',about,name='about'),
    path('gallery/',gallery,name='gallery'),
    path('stuff/',stuff,name='stuff'),
    path('blog/',blog,name='blog'),
    path('blog-single/',blog_single,name='blog-single'),
    #path('createreservation/',createreservation.as_view(),name='reservationbook'),
     path ('user/viewreservation/',viewreservation.as_view(),name='viewreservation'),
     path ('detailreservation/<int:pk>',detailreservation.as_view(),name='detail'),
     path ('deletereservation/<int:pk>',deletereservation.as_view(),name='delete'),
     path ('updatereservation/<int:pk>',updatereservation.as_view(),name='update'),
     #path ('createcontact/',createcontact.as_view(),name = "createcontactus"),
     path ('user/viewcontact/',viewcontact.as_view(),name='viewcontact'),
     path ('detailcontact/<int:pk>',detailcontact.as_view(),name='detail'),
     path ('deletecontact/<int:pk>',deletecontact.as_view(),name='delete'),
     path ('updatecontact/<int:pk>',updatecontact.as_view(),name='update'),
    #  path("user-registration/",BaseRegisterView.as_view(),name="user-registration"),
    path("user-registration/",CustomerSignUpView.as_view(),name="user-registration"),

    path('user/user-login/', UserLoginView.as_view() ,name='user-login'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
