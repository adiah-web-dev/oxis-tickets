from django.urls import path

from . import views

urlpatterns = [
	path('dashboard/', views.dashboard, name="dashboard"),
	path('', views.dashboard, name="home"),

	path('orders/', views.OrderListView.as_view(), name='orders'),
	path('order/create/', views.order_page, name="order"),
	path('order/<uuid:pk>', views.OrderDetailView.as_view(), name="order-detail"),
]
