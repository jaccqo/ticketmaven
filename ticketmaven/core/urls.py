# core/urls.py

from django.urls import path
from .views import (home,CustomAuthToken,api_docs,UserProfileRetrieveUpdateAPIView, UserProfileRetrieveUpdateDestroyAPIView,
    ActivityListCreateAPIView, ActivityRetrieveUpdateDestroyAPIView,
    TicketPurchaseListCreateAPIView, TicketPurchaseRetrieveUpdateDestroyAPIView,
     DebitCardSpendingListCreateAPIView, DebitCardSpendingRetrieveUpdateDestroyAPIView,TeamListCreateAPIView,TeamRetrieveUpdateDestroyAPIView,
     TeamsTicketPurchaseListCreateAPIView,TeamsTicketPurchaseRetrieveUpdateDestroyAPIView)

from rest_framework.schemas import get_schema_view
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly

schema_view = get_schema_view(title='API Documentation', public=True, permission_classes=[AllowAny])

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),

    path('api-documentation/', schema_view, name='api-markdown'),

    path('api/', api_docs, name='api-docs'),
    path('api/token/', CustomAuthToken.as_view(), name='api-token'),
    path('api/user-profiles/', UserProfileRetrieveUpdateAPIView.as_view(), name='user-profile-list-create'),
    path('api/user-profiles/<int:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='user-profile-retrieve-update-destroy'),
    path('api/activities/', ActivityListCreateAPIView.as_view(), name='activity-list-create'),
    path('api/activities/<int:pk>/', ActivityRetrieveUpdateDestroyAPIView.as_view(), name='activity-retrieve-update-destroy'),
    path('api/ticket-purchases/', TicketPurchaseListCreateAPIView.as_view(), name='ticket-purchase-list-create'),
    path('api/ticket-purchases/<int:pk>/', TicketPurchaseRetrieveUpdateDestroyAPIView.as_view(), name='ticket-purchase-retrieve-update-destroy'),
    path('api/debit-card-spending/', DebitCardSpendingListCreateAPIView.as_view(), name='debit-card-spending-list-create'),
    path('api/debit-card-spending/<int:pk>/', DebitCardSpendingRetrieveUpdateDestroyAPIView.as_view(), name='debit-card-spending-retrieve-update-destroy'),
    path('api/teams/', TeamListCreateAPIView.as_view(), name='team-list-create'),
    path('api/teams/<int:pk>/', TeamRetrieveUpdateDestroyAPIView.as_view(), name='team-retrieve-update-destroy'),
    path('api/teams-ticket-purchases/', TeamsTicketPurchaseListCreateAPIView.as_view(), name='teams-ticket-purchase-list-create'),
    path('api/teams-ticket-purchases/<int:pk>/', TeamsTicketPurchaseRetrieveUpdateDestroyAPIView.as_view(), name='teams-ticket-purchase-retrieve-update-destroy'),
]

