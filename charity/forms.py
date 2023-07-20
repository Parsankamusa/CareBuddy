from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Donors

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class Form(forms.ModelForm):
  class Meta:
    model = Donors
    fields = ["fullname", "mobile_number", 'donor_email',  'Donation_type', 'quantity' ]
    labels = {'fullname': "Name", "mobile_number": "Mobile Number", 'email': 'donor_email', 'type':'Donation_type', 'quantity': 'quantity'}        