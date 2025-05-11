from django.shortcuts import render


def advanced_forms(request):
	return render(request, 'theme/advanced_form.html')

def forms(request):
	return render(request, 'theme/form.html')

def buttons(request):
	return render(request, 'theme/button.html')

def modals(request):
	return render(request, 'theme/modals.html')

def invoice(request):
	return render(request, 'theme/invoice.html')

def dashboard1(request):
	return render(request, 'theme/dashboard1.html')

def order_template(request):
	return render(request, 'theme/add_ticket.html')
