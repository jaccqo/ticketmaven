# core/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_card_number = models.CharField(max_length=100, blank=True, null=True)
    cvv = models.CharField(max_length=10, blank=True, null=True)
    expiry_date = models.CharField(max_length=5, blank=True, null=True)  # Assuming MM/YY format
    expiry_year = models.CharField(max_length=4, blank=True, null=True)  # Assuming YYYY format
    card_type = models.CharField(max_length=20, blank=True, null=True)  # To store the card type

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Determine the card type based on the credit card number
        if self.credit_card_number:
            self.card_type = self._determine_card_type(self.credit_card_number)
        super().save(*args, **kwargs)

    def _determine_card_type(self, credit_card_number):
        # A simplified implementation to determine card type based on credit card number pattern
        # You may need to adjust this based on the patterns for each card type
        if credit_card_number.startswith('4'):
            return 'Visa'
        elif credit_card_number.startswith('5'):
            return 'MasterCard'
        elif credit_card_number.startswith('3'):
            return 'American Express'
        else:
            return 'Unknown'

class Activity(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class TeamsTicketPurchase(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    team = models.CharField(max_length=100)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.team} - {self.date}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Signal receiver function to save UserProfile instance when a User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()