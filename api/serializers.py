from rest_framework import serializers

from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = ['id', 'name', 'type', 'order', 'image', 'price', 'checked_in']
