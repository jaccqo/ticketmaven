# core/urls.py

from django.urls import path
from . import views

app_name = 'account' 

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'), 
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('authenticate-login/', views.authenticate_login, name='authenticate_login'),
    path('authenticate_register/', views.authenticate_register, name='authenticate_register'),
    path('logout/', views.logout_view, name='logout'),
]
