from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login

# Create your views here.
from sre_constants import SUCCESS
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.messages.views import SuccessMessageMixin
#from django.contrib.auth.mixins import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login

from UserApp.models import User
from .forms import UserForm
from django.contrib.auth.views import LoginView, LogoutView

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives


# Create your views here.
"""
class BaseRegisterView(SuccessMessageMixin, FormView):

    form_class = UserForm
    template_name = 'userportal/registration.html'
    success_url ="/user/user-login/"
  
    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)  
        user.save()    
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + " - User Created Successfully..!!"
"""
class UserLoginView(LoginView):
    template_name = 'userportal/user_login.html'
    success_url = "http://127.0.0.1:8000/a_food/view/"

#def index(request):
   # return render(request, 'userportal/index.html')



def sendmail(request):
    subject = 'welcome'
    message = 'hello world!!!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ta5.sakshi.181130116002@gmail.com','rutvikshah979@gmail.com']
    send_mail(subject,message,email_from,recipient_list)
    return HttpResponse("mail sent..")


class CustomerSignUpView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'userportal/registration.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        username=form.cleaned_data.get('username')
        password1 = form.cleaned_data.get('password1')
        dict = {'username':username, 'password1': password1}
        subject, from_email, to = 'subject', settings.EMAIL_HOST_USER, form.cleaned_data.get('email')
        html_content = render_to_string('userportal/email.html', dict)
        text_content = strip_tags(html_content)
        msg= EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return redirect('/userapp/user-login/')