from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import TruncMonth
from django.db.models import Count
from datetime import datetime

class TicketPurchase(models.Model):
    MONTH_CHOICES = [
        ('Jan', 'January'),
        ('Feb', 'February'),
        ('Mar', 'March'),
        ('Apr', 'April'),
        ('May', 'May'),
        ('Jun', 'June'),
        ('Jul', 'July'),
        ('Aug', 'August'),
        ('Sep', 'September'),
        ('Oct', 'October'),
        ('Nov', 'November'),
        ('Dec', 'December'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(default=datetime.now())
    
    ticket_type = models.CharField(max_length=100)
    month = models.CharField(max_length=3, choices=MONTH_CHOICES, editable=False)
    projection = models.IntegerField(default=0)  # Projection for the month

    def save(self, *args, **kwargs):
        # Automatically set the month abbreviation based on purchase_date
        self.month = self.purchase_date.strftime('%b')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - {self.ticket_type}'

class MonthlyTicketPurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=3, choices=TicketPurchase.MONTH_CHOICES)
    quantity = models.IntegerField(default=0)
    projection = models.IntegerField(default=0)  # Projection for the month

    class Meta:
        unique_together = ('user', 'month')

    def __str__(self):
        return f'{self.user.username} - {self.month}: {self.quantity} tickets'

class DebitCardSpending(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    week_number = models.PositiveIntegerField()
    day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES)
    merchant = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Automatically determine the day of the week
        current_date = datetime.now()
        day_of_week = current_date.strftime('%a')
        self.day_of_week = day_of_week

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - {self.merchant} - Week {self.week_number}, {self.day_of_week}'

    @classmethod
    def total_spending_per_weekday(cls, user, week_number, day_of_week):
        # Filter spending for the given user, week number, and day of the week
        spending = cls.objects.filter(
            user=user,
            week_number=week_number,
            day_of_week=day_of_week
        )
        # Calculate the total spending for the day of the week
        total_spending = spending.aggregate(models.Sum('amount'))['amount__sum'] or 0

        return total_spending