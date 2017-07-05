from django.shortcuts import render

def index(request):
	return render(request, 'website_app/index.html')