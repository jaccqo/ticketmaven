from rest_framework import serializers
from .models import TicketPurchase, DebitCardSpending

class TicketPurchaseSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = TicketPurchase
        fields = '__all__'

class DebitCardSpendingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = DebitCardSpending
        fields = '__all__'