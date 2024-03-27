from django.contrib import admin
from .models import TicketPurchase,MonthlyTicketPurchase,DebitCardSpending
# Register your models here.
admin.site.register(TicketPurchase)
admin.site.register(MonthlyTicketPurchase)
admin.site.register(DebitCardSpending)
