import email
from django import forms
from .models import User
from .models import *
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    
    # username = forms.CharField(max_length=10, required=True)
    first_name = forms.CharField(max_length=10, required=False)
    last_name = forms.CharField(max_length=10, required=False)
    email = forms.EmailField(max_length=100, help_text='Required')

    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        # self.fields['email'].widget.attrs.pop('email', None)  
        self.fields['email'].widget.attrs.update({'class': 'emailinput textinput textInput form-control', 'placeholder': 'Email'})

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        return user

class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ("username", "password", "email", "is_superuser", "is_staff", "is_active", "phone_number",)

CHOICES = (
        ("H", "Home"),
        ("W", "Work"),
    )

class AddressForm(forms.ModelForm):
    user = forms.CharField(widget = forms.TextInput(attrs = {'name' : "user"}))
    address : forms.CharField(widget = forms.TextInput(attrs = {'name' : 'address'}))
    city_name : forms.CharField(widget = forms.TextInput(attrs = {'name' : "city_name"}))
    country_name : forms.CharField(widget = forms.TextInput(attrs = {'name' : "country_name"}))
    zip_code : forms.CharField(max_length=6,widget = forms.TextInput(attrs = {'name' : "zip_code"}))
    address_type =  forms.ChoiceField(choices=CHOICES)


    class Meta:
        model = Address
        fields = ("user",  "address", "city_name", "address_type", "country_name", "zip_code", )
        # widgets = {
        #             'address' : forms.Textarea(attrs = {'name' : 'address'}),
        #             'city_name' : forms.TextInput(attrs={'name' : 'city_name'}),
        #             'country_name' : forms.TextInput(attrs= {'name' : 'country_name'}),
        #             'zip_code' : forms.TextInput(attrs= {'name' : 'zip_code'}),
        #             'address_type' :  forms.RadioSelect(choices=[CHOICES])
        # }
