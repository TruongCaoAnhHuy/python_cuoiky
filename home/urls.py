from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.get_home, name='home'),
    path('vehicles/', views.get_vehicles, name='vehicles'),
    path('services/', views.get_services, name='services'),
    path('featured/', views.get_featured, name='featured'),
    path('reviews/', views.get_reviews, name='reviews'),
    path('contact/', views.get_contact, name='contact'),
    path('login/', views.get_login.as_view(), name='login'),
    path('register/', views.get_register.as_view(), name='register'),
]