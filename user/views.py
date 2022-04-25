from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy
from .models import reservation,contact

# Create your views here.

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact1(request):
    return render(request,"contact.html")
def reservation1(request):
    return render(request,"reservation.html")
def blog(request):
    return render(request,"blog.html")
def stuff(request):
    return render(request,"stuff.html")
def gallery(request):
    return render(request,"gallery.html")
def menu(request):
    return render(request,"menu.html")
def blog(request):
    return render(request,"blog.html")
def blog_single(request):
    return render(request,"blog-single.html")
def normalindex(request):
    return render(request,"normalindex.html")
#--------------------------------------RESERVATION CRUD-----------------------------------------
class createreservation(CreateView):
    model = reservation
    fields = '__all__'
    template_name = 'reservation/createreservation.html'
    success_url = '/user/viewreservation/'
class viewreservation(ListView):
    model = reservation
    reservations = model.objects.all()
    context_object_name = 'reservations'
    template_name = "reservation/list.html"
class detailreservation(DetailView):
    model = reservation
    #template_name = "user//template/detail.html"
class deletereservation(DeleteView):
    model = reservation
    fields = '__all__'
    #template_name = 'user//template/delete.html'
    # success_url='/user/view/'
class updatereservation(UpdateView):
    model = reservation
    fields = '__all__'
    #template_name = 'user//template/update.html'
    # success_url='/user/view/'
#-------------------------------------- CRUD-----------------------------------------
class createcontact(CreateView):
    model = contact
    fields='__all__'
    template_name='contact/createcontact.html'
    success_url='/user/viewcontact/'
class viewcontact(ListView):
    model = contact
    contactes = model.objects.all()
    context_object_name = 'contactes'
    template_name = "contact/contactlist.html"
class detailcontact(DetailView):
    model = contact
    #template_name = "a_food/detail.html"
class deletecontact(DeleteView):
    model = contact
    fields='__all__'
    #template_name='a_food/delete.html'
    #success_url='/a_food/view/'
class updatecontact(UpdateView):
    model = contact
    fields='__all__'
    #template_name='a_food/update.html'
    #success_url='/a_food/view/'

