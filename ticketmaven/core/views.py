from django.shortcuts import render,redirect
from django.urls import reverse
from rest_framework import generics
from .models import UserProfile, Activity, TeamsTicketPurchase
from .serializers import UserProfileSerializer, ActivitySerializer, TeamsTicketPurchaseSerializer
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication 
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, status

from dashboard.models import TicketPurchase, DebitCardSpending
from dashboard.serializers import TicketPurchaseSerializer, DebitCardSpendingSerializer


from account.models import Team
from account.serializers import TeamSerializer
import datetime

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


def home(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard:dash'))
    else:
     
        return render(request, 'core/home.html')

def api_docs(request):
    return render(request, 'core/api-docs.html')

class UserProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]  
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Get the user profile object for the logged-in user
        queryset = self.get_queryset()
        obj = queryset.filter(user=self.request.user).first()
        return obj

class UserProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
 
    serializer_class = UserProfileSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserProfile.objects.filter(user=user)
    
    def perform_create(self, serializer):
        # Automatically set the user profile to the logged-in user's profile
        serializer.save(user=self.request.user)

class ActivityListCreateAPIView(generics.ListCreateAPIView):
 
    serializer_class = ActivitySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        profile=UserProfile.objects.get(user=user)
        return Activity.objects.filter(user_profile=profile)
    
    def perform_create(self, serializer):
        # Automatically set the user profile to the logged-in user's profile
        serializer.save(user_profile=self.request.user.userprofile)

class ActivityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
   
    serializer_class = ActivitySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        profile=UserProfile.objects.get(user=user)

        return Activity.objects.filter(user_profile=profile)
    
    def perform_create(self, serializer):
            # Automatically set the user profile to the logged-in user's profile
            serializer.save(user_profile=self.request.user.userprofile)

class TeamsTicketPurchaseListCreateAPIView(generics.ListCreateAPIView):
    
    serializer_class = TeamsTicketPurchaseSerializer
    authentication_classes =[TokenAuthentication, SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        profile=UserProfile.objects.get(user=user)
        return TeamsTicketPurchase.objects.filter(user_profile=profile)
    
    

class TeamsTicketPurchaseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = TeamsTicketPurchaseSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        profile=UserProfile.objects.get(user=user)
        return TeamsTicketPurchase.objects.filter(user_profile=profile)
    
    def perform_create(self, serializer):
            # Automatically set the user profile to the logged-in user's profile
            serializer.save(user_profile=self.request.user.userprofile)

class TicketPurchaseListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = TicketPurchaseSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]  
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return TicketPurchase.objects.filter(user=user)
    

    def perform_create(self, serializer):
        # Check if there is an existing record for the same user, ticket type, and month
        # Get current date and time
        now = datetime.datetime.now()

        # Format the month as a three-letter abbreviation
        month_str = now.strftime('%b')

        existing_record = TicketPurchase.objects.filter(
            user=self.request.user,
            month=month_str
        ).first()

        if existing_record:
            # If an existing record is found, update the quantity and projection
            existing_record.quantity += int(self.request.data.get('quantity', 0))
            existing_record.projection += int(self.request.data.get('projection', 0))
            existing_record.save()
            serializer.instance = existing_record
        else:
            # If no existing record is found, create a new record
            serializer.save(user=self.request.user)

        # Return the response with the serializer instance
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TicketPurchaseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = TicketPurchaseSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return TicketPurchase.objects.filter(user=user)

    def perform_create(self, serializer):
        # Automatically set the user profile to the logged-in user's profile
        serializer.save(user=self.request.user)


class DebitCardSpendingListCreateAPIView(generics.ListCreateAPIView):
 
    serializer_class = DebitCardSpendingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return DebitCardSpending.objects.filter(user=user)
    
    def perform_create(self, serializer):
        # Automatically set the user profile to the logged-in user's profile
        serializer.save(user=self.request.user)

class DebitCardSpendingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = DebitCardSpendingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return DebitCardSpending.objects.filter(user=user)
    
    def perform_create(self, serializer):
        # Automatically set the user profile to the logged-in user's profile
        serializer.save(user=self.request.user)

# List and Create API view for Team model
class TeamListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = TeamSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Team.objects.filter(user=user)
    
    def perform_create(self, serializer):
        # Automatically set the user profile to the logged-in user's profile
        serializer.save(user=self.request.user)

# Retrieve, Update, and Destroy API view for Team model
class TeamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TeamSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]  
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Team.objects.filter(user=user)
    
    def perform_create(self, serializer):
        # Automatically set the user profile to the logged-in user's profile
        serializer.save(user=self.request.user)