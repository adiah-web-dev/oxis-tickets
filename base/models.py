import uuid
from datetime import date

from django.db import models

# TODO Maybe slugify the names?

class Event(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	name = models.CharField(max_length=200)
	theme = models.CharField(max_length=100, blank=True, null=True, default="")
	date = models.DateField(default=date.today)
	# time = ?

	def __str__(self):
		return f"{self.name} - {self.theme}"

class EventTicket(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
	image = models.ImageField(upload_to='eventTickets/', blank=True, null=True)
	type = models.CharField(max_length=100, default="General")
	price = models.IntegerField()

	def __str__(self):
		return f"{self.event.name} - {self.type}"
