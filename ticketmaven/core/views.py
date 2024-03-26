from django.shortcuts import render,redirect
from django.urls import reverse

def home(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard:dash'))
    else:
     
        return render(request, 'core/home.html')


