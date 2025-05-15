import qrcode
from django.conf import settings
from django.core.files import File
from django.shortcuts import redirect, render
from django.views import generic
from PIL import Image

from .models import Order, Ticket

ROOT = settings.BASE_DIR


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
			print(new_ticket)

			# Open the base image and copy it so it's not overwritten
			img = Image.open(ROOT / 'static/img/grad-ticket.png')
			img_bg = img.copy()

			qr = qrcode.QRCode(
				box_size=10,
				version=1
			)

			qr.add_data(new_ticket.id)
			qr.make()
			img_qr = qr.make_image(fill_color="#440972", back_color="#ffffff")
			img_qr.save(ROOT / 'media/temp/qrcode_inset.png')

			qr_inset = Image.open(ROOT / 'media/temp/qrcode_inset.png')
			img_bg.paste(qr_inset, (50, 200))
			img_bg.save(ROOT / 'media/temp/ticket.png')

			new_ticket.image.save(f'{new_ticket.name}--{new_ticket.id}.png', File(open(ROOT / 'media/temp/ticket.png', 'rb')))

			order.ticket_set.add(new_ticket)

		# url = reverse('orders')
		# return JsonResponse({"url": url}, status=201)
		return redirect('orders')

	return render(request, 'tickets/new_order.html')
