from django.shortcuts import render
from django.views import generic

from tickets.models import Ticket


# Create your views here.
def scanner(request):
	return render(request, 'scanner/scan.html')

# def scanned_ticket(request, pk):
# 	print(pk)
# 	return render(request, 'scanner/ticket.html')

class TicketDetailView(generic.DetailView):
	model = Ticket
