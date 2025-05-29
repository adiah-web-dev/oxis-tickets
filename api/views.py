from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tickets.models import Ticket

from .serializers import TicketSerializer


class TicketList(generics.ListAPIView):
	queryset = Ticket.objects.all()
	serializer_class = TicketSerializer

class TicketDetail(generics.RetrieveUpdateAPIView):
	queryset = Ticket.objects.all()
	serializer_class = TicketSerializer
