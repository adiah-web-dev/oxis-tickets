from django.contrib import admin

from .models import Email, Order, Ticket


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('name', 'id', 'date', 'email_address', 'phone', 'total', 'paid')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
	list_display = ('name', 'id', 'type', 'price', 'image')

	# Add a link back to the order

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
	list_display = ('to_email', 'status', 'created_at')
