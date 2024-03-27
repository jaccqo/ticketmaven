# Serializer for Team model
from rest_framework import serializers, generics

from account.models import Team

class TeamSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Team
        fields = "__all__"
