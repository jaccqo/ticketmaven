from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard:dash'))
    return render(request, 'account/signin.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard:dash'))
    return render(request, 'account/signup.html')

def forgot_password_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard:dash'))
    return render(request, 'account/forgot_password.html')

def terms_and_conditions(request):
    return render(request, 'account/terms_and_conditions.html')



def authenticate_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        
        if email and password:
            # Check if user exists in the database
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                # Return error response if user doesn't exist
                return JsonResponse({'status': 'error', 'message': 'Invalid email or password'})

            # Check if the user is active
            if not user.is_active:
                return JsonResponse({'status': 'error', 'message': 'Your account is pending approval. Please wait for admin approval.'})

            # Authenticate user
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                # Login user
                login(request, user)

                # Optionally, handle remember me functionality
                if remember == "true":
                    # Set session expiration to 3 months (90 days)
                    request.session.set_expiry(settings.SESSION_COOKIE_AGE_REMEMBER)

                # Return success response
                redirect_url = reverse('dashboard:dash')
                return JsonResponse({'status': 'success', 'message': 'Login successful', 'redirect_url': redirect_url})
            else:
                # Return error response if authentication fails
                return JsonResponse({'status': 'error', 'message': 'Invalid email or password'})
        else:
            # Return error response if email or password is missing
            return JsonResponse({'status': 'error', 'message': 'Please provide both email and password'})
    else:
        # If the request method is not POST, return an error response
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def authenticate_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if email is already in use
        if User.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', 'message': 'Email already exists'})
        
        # Create the user with is_active set to False
        user = User.objects.create_user(username=email, email=email, password=password, is_active=False)
        user.first_name = name
        user.save()
        
        # Send notification to admin for approval (you need to implement this)
        # For example, send an email to the admin with the details of the new user
        
        return JsonResponse({'status': 'success', 'message': 'User registered successfully. Waiting for admin approval.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
def logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout (e.g., home page)
    return redirect('core:home')
