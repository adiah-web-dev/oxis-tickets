from django.conf import settings
from django.core.files import File
from django.shortcuts import redirect, render
from django.views import generic

from .models import Email, Order, Ticket
from .utils.email_utils import send_email
from .utils.image_utils import create_image

ROOT = settings.BASE_DIR

def dashboard(request):
	orders = Order.objects.all()[:10]
	tickets = Ticket.objects.all()
	email_count = Email.objects.filter(status='sent').count()

	total = 0
	for ticket in tickets:
		total += ticket.price


	ticketCount = tickets.count()

	context = {
		'orders': orders,
		'ticketCount': ticketCount,
		'income': total,
		'emailCount': email_count,
	}
	print(settings.EMAIL_HOST_USER)

	return render(request, 'tickets/dashboard.html', context)

# Orders

class OrderListView(generic.ListView):
	model = Order
	paginate_by = 20

class OrderDetailView(generic.DetailView):
	model = Order

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
			email_address=email,
			phone=phone,
		)
		order.save()

		total = 0

		# loop over the tickets
		for i in range(ticket_count):
			ticket_name = request.POST[f'ticketName{i}']
			ticket_type = request.POST[f'ticketType{i}']

			new_ticket = Ticket(
				name=ticket_name,
				type=ticket_type
			)
			new_ticket.save()
			total += new_ticket.price

			create_image(ticket_name, ticket_type, new_ticket.id)

			# Save the created image to database
			new_ticket.image.save(f'{new_ticket.name}--{new_ticket.id}.png', File(open(ROOT / 'media/temp/ticket_text.png', 'rb')))

			order.ticket_set.add(new_ticket)

		send_email(order)

		return redirect('orders')

	return render(request, 'tickets/new_order.html')
