from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.booking, name='booking_page'),
    url(r'^post_booking$', views.post_booking, name='post_booking'),
]
