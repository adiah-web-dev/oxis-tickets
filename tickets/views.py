import json

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

from .models import Order, Ticket


class OrderListView(generic.ListView):
	model = Order
	paginate_by = 20

def order_page(request):

	# Saving an order has to be done by POST
	if request.method == "POST":

		# Get the details of the tickets
		name = request.POST["full_name"]
		email = request.POST["email"]
		phone = request.POST["phone"]
		ticket_count = int(request.POST["ticketCount"])

		# Attempt to create a new Order and then add the tickets to it
		order = Order(
			name=name,
			email=email,
			phone=phone,
		)
		order.save()

		# loop over the tickets
		for i in range(ticket_count):
			ticket_name = request.POST[f'ticketName{i}']
			ticket_type = request.POST[f'ticketType{i}']

			new_ticket = Ticket(
				name=ticket_name,
				type=ticket_type
			)
			new_ticket.save()

			order.ticket_set.add(new_ticket)

		# url = reverse('orders')
		# return JsonResponse({"url": url}, status=201)
		return redirect('orders')

	return render(request, 'tickets/new_order.html')
