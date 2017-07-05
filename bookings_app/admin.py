from django.contrib import admin
from .models import Booking, Treatment, Therapist

admin.site.register(Booking)
admin.site.register(Treatment)
admin.site.register(Therapist)