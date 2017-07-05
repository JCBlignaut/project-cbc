from django import forms
from datetime import datetime
from .models import Booking, Treatment, Therapist

class BookingForm(forms.ModelForm):
	client_name = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control input-lg form-input-shadow',
			'placeholder': 'Name...',
		}
	))
	client_email = forms.EmailField(widget=forms.TextInput(
		attrs={
			'class': 'form-control input-lg form-input-shadow',
			'placeholder': 'Email...',
		}
	))
	treatment = forms.ModelChoiceField(widget=forms.Select(
		attrs={
			'class': 'form-control input-lg form-input-shadow',
			'placeholder': 'Treatment...',
		}),
		queryset = Treatment.objects.all(),
	)
	therapist = forms.ModelChoiceField(widget=forms.Select(
		attrs={
			'class': 'form-control input-lg form-input-shadow',
			'placeholder': 'Treatment...',
		}),
		queryset = Therapist.objects.all(),
		empty_label="No preference",
		required = False,
	)
	booking_date = forms.DateField(widget=forms.DateInput(
		attrs={
			'class': 'form-control input-lg form-input-shadow',
			'placeholder': 'DD/MM/YYYY',
		}
	))
	booking_time = forms.TimeField(widget=forms.TimeInput(
		attrs={
			'class': 'form-control input-lg form-input-shadow',
			'placeholder': 'HH:MM',
		}
	))
	
	class Meta:
		model = Booking
		fields = '__all__'