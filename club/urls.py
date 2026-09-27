from django.urls import path
from . import views

app_name = 'club'

urlpatterns = [
    path('', views.home, name='home'),
    path('tariffs/', views.tariffs_list, name='tariffs'),
    path('tariffs/new/', views.tariff_create, name='tariff_create'),
    path('tariffs/<int:pk>/edit/', views.tariff_edit, name='tariff_edit'),
    path('services/', views.services_list, name='services'),
    path('services/new/', views.service_create, name='service_create'),
    path('computers/', views.computers_list, name='computers'),
    path('clients/', views.clients_list, name='clients'),
    path('clients/new/', views.client_create, name='client_create'),
]
