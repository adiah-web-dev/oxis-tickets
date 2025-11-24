from django.contrib import admin

from .models import Event, EventTicket


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'theme', 'id', 'date')
	ordering = ['date']

@admin.register(EventTicket)
class EventTicketAdmin(admin.ModelAdmin):
	list_display = ('event', 'id', 'type', 'price')
	ordering = ['event']
