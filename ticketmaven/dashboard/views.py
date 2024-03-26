from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from account.models import Team
import json
from django.http import JsonResponse
from django.db import IntegrityError
import time
import requests
import threading
from core.models import UserProfile,Activity,TicketPurchase


@login_required(login_url='account:login')
def dashboard_view(request):
    # Retrieve teams for the current user
    teams = Team.objects.filter(user=request.user)

    # Retrieve user's profile
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    # Retrieve user's activity
    if user_profile:
        user_activity = Activity.objects.filter(user_profile=user_profile)
        ticket_purchases = TicketPurchase.objects.filter(user_profile=request.user.userprofile)
    else:
        user_activity = None


    # Render the template with the teams, user's profile, and activity data
    return render(request, 'dashboard/dashboard.html', {'teams': teams, 'user_profile': user_profile, 'user_activity': user_activity,'ticket_purchases': ticket_purchases})

@login_required(login_url='account:login')
def add_team(request):
    if request.method == 'POST':
        # Load the JSON data from the request body
        data = json.loads(request.body)
        name = data.get('name')
        tickets = data.get('tickets')
        
        # Assuming request.user is authenticated and contains the current user
        user = request.user
        
        try:
            # Create the new team object
            existing_team = Team.objects.filter(user=user, name=name)
            if existing_team:
                return JsonResponse({'success': False, 'message': f'Team ({name}) name must be unique'}, status=400)
            
            else:
                team = Team.objects.create(user=user, name=name, tickets=tickets, current_tickets_count=0)

            return JsonResponse({'success': True, 'message': f'{name.capitalize()} added successfully', 'team_name': team.name, 'team_id': team.id})
        except Exception as e:
            print(e)
            # Handle the case where a team with the same name already exists
            return JsonResponse({'success': False, 'message': f'{str(e)}'}, status=400)
    else:
        # Return a JSON response indicating failure for non-POST requests
        return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)


@login_required(login_url='account:login')
def update_team_slider(request):
    if request.method == 'POST':
        # Parse JSON data from request body
        data = json.loads(request.body)
        
        # Extract data from the request
        team_name = data.get('team_name')
        new_slider_value = data.get('new_slider_value')
        team_username = data.get('username')
        team_password = data.get('password')
        
        try:
            # Get the team
            team = Team.objects.get(user=request.user,name=team_name)
            
            # Update the slider value
            team.tickets = new_slider_value
            
            # Update the username and password
            if team_username:
                team.username = team_username
            if team_password:
                team.password = team_password
            
            # Save the changes
            team.save()
            
            # Return success response
            return JsonResponse({'success': True, 'message': f'{team_name} tickets value updated successfully'})
        except Team.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Team not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)

    

@login_required(login_url='account:login')
def delete_team(request):
    # Get the team name from the POST data
    data = json.loads(request.body)
    team_name = data.get('team_name')

    # Perform deletion operation
    try:
        team = Team.objects.get(user=request.user,name=team_name)
        team.delete()
        return JsonResponse({'success': True, 'message': 'Team deleted successfully'})
    except Team.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Team not found'}, status=404)



def perform_automation(request,team_name, action):
    # Define the API endpoint
    api_url = 'https://httpbin.org/post'  # Replace with your actual API endpoint
    
    # Define the data to be sent in the request
    data = {'team_name': team_name}
    
    # Determine the URL based on the action
    if action == 'start':
        # url = api_url + '/start'
        automated=True

    elif action == 'stop':
        # url = api_url + '/stop'
        automated=False
     
    else:
        return {'success': False, 'message': 'Invalid action'}
    
    # Make the API call
    response = requests.post(api_url, data=data)
    
    # Check if the API call was successful
    if response.status_code == 200:
        # Update the database
        try:
            team = Team.objects.get(user=request.user,name=team_name)

            
            if automated:
                team.is_automated=automated
                team.save()
                return {'success': True, 'message': 'Automation ' + action + 'ed successfully', 'team_name': team_name}
            else:
                team.is_automated=automated
                team.save()
                return {'success': True, 'message': 'Automation ' + action + 'ed successfully', 'team_name': team_name}
            
        except Team.DoesNotExist:
            return {'success': False, 'message': 'Team not found'}
    else:
        return {'success': False, 'message': 'Failed to ' + action + ' automation'}
    
@login_required(login_url='account:login')
def update_automation_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        team_name = data.get('team_name')
        action = data.get('action')  # Get the action parameter
        
        # Enqueue the task
        resp=perform_automation(request,team_name, action)
        print(resp)
        
        return JsonResponse(resp)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)
    


def store_credit_card(request):
    data = json.loads(request.body)
    credit_card_number = data.get('credit_card_number')
    cvv = data.get('cvv')

    # Assuming the user is authenticated, get the UserProfile instance
    user_profile = UserProfile.objects.get(user=request.user)

    # Update the UserProfile with the credit card information
    user_profile.credit_card_number = credit_card_number
    user_profile.cvv = cvv
    user_profile.save()

    return JsonResponse({'success': True})