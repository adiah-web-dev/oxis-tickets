from django.shortcuts import redirect, render
from django.views import generic

from tickets.models import Ticket


# Create your views here.
def scanner(request):
	return render(request, 'scanner/scan.html')

# def scanned_ticket(request, pk):
# 	print(pk)
# 	return render(request, 'scanner/ticket.html')

def check_in(request, ticket_id):
	# if request.method == 'POST':
	# 	# print the status
	# 	print(ticket_id)
	# 	return redirect('scanned_ticket', pk=ticket_id)
	print(ticket_id)
	return redirect('scanned-ticket', pk=ticket_id)

class TicketDetailView(generic.DetailView):
	model = Ticket
