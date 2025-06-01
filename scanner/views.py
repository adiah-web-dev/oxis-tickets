from django.shortcuts import render


# Create your views here.
def scanner(request):
	return render(request, 'scanner/scan.html')

def scanned_ticket(request, pk):
	print(pk)
	return render(request, 'scanner/ticket.html')
