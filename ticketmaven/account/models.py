from django.db import models

# Create your models here.

from django.contrib.auth.models import User
class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tickets = models.IntegerField()
    current_tickets_count = models.IntegerField(default=0)
    is_automated = models.BooleanField(default=False)
    username = models.CharField(max_length=100,null=True,blank=True)  # New field for username
    password = models.CharField(max_length=100,null=True,blank=True)  # New field for password

    def __str__(self):
        return self.name
    

