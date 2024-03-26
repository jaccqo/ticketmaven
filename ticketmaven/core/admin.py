from django.contrib import admin
from .models import UserProfile,Activity,TicketPurchase
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(TicketPurchase)