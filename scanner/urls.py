from django.urls import path

from . import views

urlpatterns = [
	path('', views.scanner, name='scanner'),
	# path('tickets/<uuid:pk>/', views.scanned_ticket, name='scanned-ticket'),
	path('tickets/<uuid:pk>/', views.TicketDetailView.as_view(), name='scanned-ticket'),
	path('tickets/<uuid:ticket_id>/check-in/', views.check_in, name='check-in'),
]
