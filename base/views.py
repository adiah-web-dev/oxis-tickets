from django.shortcuts import render

from .models import Event


def home(request):
	events = Event.objects.all()[:10]

	context = {
		'events': events,
	}

	return render(request, 'base/home.html', context)
