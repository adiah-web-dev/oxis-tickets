from django.urls import path

from . import views

urlpatterns = [
	path('dashboard/', views.dashboard, name="dashboard"),
	# path('', views.dashboard, name="home"),

	# Event specific urls
	path('event/<uuid:event_id>', views.event_dash, name="event"),
	path('order/<uuid:event_id>/create', views.event_order, name="new-order"),


	path('orders/', views.OrderListView.as_view(), name='orders'),
	path('order/create/', views.order_page, name="order"),

	path('order/<uuid:pk>', views.OrderDetailView.as_view(), name="order-detail"),
]
