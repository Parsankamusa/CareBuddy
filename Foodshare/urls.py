"""
URL configuration for Foodshare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.urls import path, include
#from charity.views import manage
urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include('charity.urls')),
    #path('accounts/', include('accounts.urls')),
    #path('manage/', manage.as_view(), name='manage'),
    #path('', about.as_view(), name='about'),
    #path('login/', login.as_view(), name='login'),
    #path('signup/', signup.as_view(), name='signup'),
    #path('Donation/', Donation.as_view(), name='Donation'),
    #path('', contact.as_view(), name='contact'),
    ] 
    