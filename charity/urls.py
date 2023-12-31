from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .views import  manageTemplateView, DonationTemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('Form/', views.profile, name='Form'),
    path('login/', auth_view.LoginView.as_view(template_name='charity/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='charity/logout.html'), name="logout"),
    path('manage-Donations/', manageTemplateView.as_view(), name='manage'),
    path('make-Donation/', DonationTemplateView.as_view(), name='Donation'),
    ]
