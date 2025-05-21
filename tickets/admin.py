from django.contrib import admin

from .models import Order, Ticket


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('name', 'id', 'date', 'email', 'phone', 'total', 'paid')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
	list_display = ('name', 'id', 'type', 'price', 'image')

	# Add a link back to the order
