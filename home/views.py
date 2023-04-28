from django.shortcuts import render
from .form import LoginForm, RegisterForm
from django.views import View

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

class get_login(View):
    def get(self, request):
        lG = LoginForm
        return render(request, 'home/login.html', {'lG': lG})
    
class get_register(View):
    def get(self, request):
        rG = RegisterForm
        return render(request, 'home/register.html', {'rG': rG})

# def get_register(request):
#     return render (request, 'home/register.html')