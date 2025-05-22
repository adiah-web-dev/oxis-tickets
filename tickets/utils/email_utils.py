import logging

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.timezone import now

from ..models import Email

logger = logging.getLogger(__name__)


def send_email(order):
	subject = "🎓 Your Graduation Tickets – Oxbridge International School | Enchanted Garden"
	html_content = render_to_string('tickets/email_template.html', {
		"customer_name": order.name,
		"tickets": order.ticket_set.all(),
		"total": order.total,
	})
	text_content = strip_tags(html_content)

	email = Email(
		subject=subject,
		body=text_content,
		to_email=order.email_address,
		order=order
	)
	email.save()

	try:
		msg = EmailMultiAlternatives(
			subject,
			text_content,
			settings.EMAIL_HOST_USER,
			[order.email_address],
			bcc=['adiahnat@gmail.com']
		)
		msg.attach_alternative(html_content, "text/html")

		for ticket in order.ticket_set.all():
			image_file = ticket.image.read()
			image_name = ticket.image.name
			msg.attach(image_name, image_file, 'image/png')

		msg.send()

		email.status = 'sent'
		email.sent_at = now()
		email.error_message = ''

	except Exception as e:
		error_msg = str(e)
		logger.error(f"Failed to send email to {email.order__email}: {error_msg}")
		email.status = 'failed'
		email.error_message = error_msg

	finally:
		email.save()
