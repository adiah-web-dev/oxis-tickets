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

class Ticket(models.Model):
	TYPES = (
		("p", "Parent"),
		("g", "Graduating"),
		("ge", "Graduating Early Years"),
		("ng", "Non-graduating"),
		("d", "Learner's Date"),
	)

	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	name = models.CharField(max_length=200)
	type = models.CharField(max_length=3, choices=TYPES, default="g")
	order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return f"{self.name} - {self.type}"
