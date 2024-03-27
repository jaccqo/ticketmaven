# core/serializers.py
from rest_framework import serializers
from .models import UserProfile, Activity, TeamsTicketPurchase

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = UserProfile
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    user_profile = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Activity
        fields = '__all__'

class TeamsTicketPurchaseSerializer(serializers.ModelSerializer):
    user_profile = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = TeamsTicketPurchase
        fields = '__all__'
