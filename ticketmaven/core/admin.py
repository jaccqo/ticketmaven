from django.contrib import admin
from .models import UserProfile,Activity,TeamsTicketPurchase
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(TeamsTicketPurchase)