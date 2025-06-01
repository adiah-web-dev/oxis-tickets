from django.urls import path

from . import views

urlpatterns = [
	path('', views.scanner, name='scanner'),
	path('tickets/<uuid:pk>/', views.scanned_ticket, name='scanned-ticket'),
]
