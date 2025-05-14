from django.contrib import admin

from .models import Order, Ticket


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('name', 'id', 'date', 'email', 'phone', 'paid')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
	list_display = ('name', 'id', 'type')

	# Add a link back to the order
