from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.staff_index, name='staff_index'),
]