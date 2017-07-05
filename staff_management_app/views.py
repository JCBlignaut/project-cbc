from django.shortcuts import render

def staff_index(request):
	return render(request, 'staff_management_app/staff_index.html')
