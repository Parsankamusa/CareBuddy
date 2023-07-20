from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
#from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Donors
from .forms import  Form

# create the form rendering here

def index(request):
    return render(request, 'charity/index.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('index')
    else:
        form = UserRegisterForm()

    return render(request, 'charity/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'charity/profile.html')


    
# Create your views here.
def Form(request):
  if request.method == "POST":
    form = Form(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = form()
  return render(request, 'Charity/Form', {'form': form})