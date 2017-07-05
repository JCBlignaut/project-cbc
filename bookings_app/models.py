from django.db import models

class Booking(models.Model):
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	client_name = models.CharField(max_length=128)
	client_email = models.EmailField(max_length=254)
	treatment = models.ForeignKey(
		'Treatment',
		on_delete = models.CASCADE,
	)
	therapist = models.ForeignKey(
		'Therapist',
		on_delete = models.CASCADE,
		null=True,
		blank = True,
	)
	booking_date = models.DateField()
	booking_time = models.TimeField()

	def __str__(self):
		return("{} - {}, {} @ {}".format(self.timestamp, self.client_name, self.booking_date, self.booking_time))

class Treatment(models.Model):
	timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
	treatment_name = models.CharField(max_length=128)
	duration = models.DurationField()
	therapist = models.ManyToManyField('Therapist')
	price = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return("Name: {}, Length: {}, Price: {}".format(self.treatment_name, self.duration, self.price))

class Therapist(models.Model):
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	therapist_name = models.CharField(max_length=128)
	therapist_surname = models.CharField(max_length=128)
	contact_number = models.IntegerField()
	email = models.EmailField(max_length=254)
	title = models.CharField(max_length=128)

	def __str__(self):
		return("{} {}".format(self.therapist_name, self.therapist_surname))