import qrcode
from django.conf import settings
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import generic
from PIL import Image, ImageDraw, ImageFont

from .models import Order, Ticket
from .utils.email_utils import send_email

ROOT = settings.BASE_DIR

def dashboard(request):
	orders = Order.objects.all()[:10]
	tickets = Ticket.objects.all()

	total = 0
	for ticket in tickets:
		total += ticket.price


	ticketCount = tickets.count()

	context = {
		'orders': orders,
		'ticketCount': ticketCount,
		'income': total,
	}
	print(settings.EMAIL_HOST_USER)

	return render(request, 'tickets/dashboard.html', context)

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



def create_image(name, type, id):
	template = ''

	match type:
		case "p":
			template = "Parent"
		case "g":
			template = "Graduate"
		case "ge":
			template = "Early"
		case "ng":
			template = "Student"
		case "d":
			template = "Plus"

	img = Image.open(ROOT / f'static/img/grad_tickets/{template}.png')
	img_bg = img.copy()

	qr = qrcode.QRCode(
		box_size=4,
		version=1
	)

	qr.add_data(id)
	qr.make()

	img_qr = qr.make_image(fill_color='black', back_color='white')
	img_qr.save(ROOT / 'media/temp/qrcode_inset.png')

	qr_inset = Image.open(ROOT / 'media/temp/qrcode_inset.png')

	x = img_bg.width - (qr_inset.width + 44)
	y = img_bg.height - (qr_inset.height + 230)

	img_bg.paste(qr_inset, (x, y))
	img_bg.save(ROOT / 'media/temp/ticket.png')

	# Add text
	image = Image.open(ROOT / 'media/temp/ticket.png')
	draw = ImageDraw.Draw(image)

	font = ImageFont.truetype(ROOT / 'static/fonts/RobotoSlab.ttf', 44)
	text_color = 'white'
	name_length = draw.textlength(name, font)

	x = (image.width - name_length) / 2
	y = image.height / 2 + 160
	name_position = (x, y)

	draw.text(name_position, name, fill=text_color, font=font)
	image.save(ROOT / 'media/temp/ticket_text.png')
