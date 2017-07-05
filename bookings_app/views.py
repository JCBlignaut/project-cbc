from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BookingForm

def booking(request):
	form = BookingForm()
	return render(request, 'bookings_app/booking_page.html', {'form':form})

def post_booking(request):
	form = BookingForm(request.POST)
	if form.is_valid():
		form.save(commit=True)
		return HttpResponseRedirect('/')
	return render(request, 'bookings_app/booking_page.html', {'form': form})