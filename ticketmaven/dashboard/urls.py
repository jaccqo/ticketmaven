from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard_view, name='dash'),
    path('add/', views.add_team, name='add_team'),
    path('update_team_slider/', views.update_team_slider, name='update_team_slider'),
    path('delete_team/', views.delete_team, name='delete_team'),
    path('update_automation_status/', views.update_automation_status, name='update_automation_status'),
    path('store_credit_card/', views.store_credit_card, name='store_credit_card'),
]
