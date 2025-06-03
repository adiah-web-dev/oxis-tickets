import uuid
from datetime import date

from django.db import models
from django.urls import reverse


class Order(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	date = models.DateField(default=date.today)
	name = models.CharField(max_length=200)
	email_address = models.CharField(max_length=200)
	phone = models.CharField(max_length=20)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return f"{self.date} - {self.name}"

	def get_absolute_url(self):
		""""Returns the URL to access a particular author instance."""
		return reverse('order-detail', args=[str(self.id)])

	# Create some method here to get the total of an order based on the number of tickets
	@property
	def total(self):
		"""Calculates the combined price of tickets in one order"""
		sum = 0
		for ticket in self.ticket_set.all():
			sum += ticket.price

		return sum
		# return self.aggregate(models.Sum('price'))['price__sum'] or 0
		# return self.objects.aggregate(models.Sum('ticket__price'))

	@property
	def ticket_count(self):
		"""Calculates the total number of tickets in order"""
		return self.ticket_set.all().count()

class Ticket(models.Model):
	TYPES = (
		("p", "Parent"),
		("g", "Graduate"),
		("ge", "Early Years Graduate"),
		("ng", "Learner"),
		("d", "Plus One"),
		("pk", "Plus One (Child)")
	)

	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	name = models.CharField(max_length=200)
	type = models.CharField(max_length=3, choices=TYPES, default="g")
	order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
	image = models.ImageField(upload_to='tickets/', blank=True, null=True)

	def __str__(self):
		return f"{self.name} - {self.type}"

	@property
	def price(self):
		"""Determines the price of a ticket based on the ticket type"""
		cost = 0
		match self.type:
			case "p":
				cost = 125
			case "g":
				cost = 550
			case "ge":
				cost = 250
			case "ng":
				cost = 100
			case "d":
				cost = 250
			case "pk":
				cost = 100

		return cost

class Email(models.Model):
	STATUS_CHOICES = [
		('pending', 'Pending'),
		('sent', 'Sent'),
		('failed', 'Failed'),
	]

	to_email = models.EmailField(null=True, blank=True)
	subject = models.CharField(max_length=255)
	body = models.TextField()
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
	error_message = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	sent_at = models.DateTimeField(null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return f"Email to {self.to_email} - {self.status}"
