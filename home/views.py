from django.shortcuts import render

# Create your views here.
def get_home(request):
    return render (request, 'home/home.html')

def get_vehicles(request):
    return render (request, 'home/vehicles.html')

def get_services(request):
    return render (request, 'home/services.html')

def get_featured(request):
    return render (request, 'home/featured.html')

def get_reviews(request):
    return render (request, 'home/reviews.html')

def get_contact(request):
    return render (request, 'home/contact.html')

def get_login(request):
    return render (request, 'home/login.html')

def get_register(request):
    return render (request, 'home/register.html')