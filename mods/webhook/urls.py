from django.urls import path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('facebook/', views.FacebookWebhookView.as_view(), name='facebook'),
    path('resolver/', views.ResolverWebhookView.as_view(), name='resolver'),
    path('ticketupdate/', views.TicketUpdateView.as_view(), name='ticketupdate'),
]