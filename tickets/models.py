import uuid
from datetime import date

from django.db import models


class Order(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	date = models.DateField(default=date.today)
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=20)
	paid = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.date} - {self.name}"

	# Create some method here to get the total of an order based on the number of tickets
	# @property
	# def total(self):
		# """Calculates the combined price of tickets in one order"""
		# return self.aggregate(models.Sum('price'))['price__sum'] or 0
		# return self.objects.aggregate(models.Sum('ticket__price'))

class Ticket(models.Model):
	TYPES = (
		("p", "Parent"),
		("g", "Graduate"),
		("ge", "Early Years Graduate"),
		("ng", "Student"),
		("d", "Plus One"),
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
				cost = 150
			case "g":
				cost = 550
			case "ge":
				cost = 250
			case "ng":
				cost = 100
			case "d":
				cost = 250

		return cost
