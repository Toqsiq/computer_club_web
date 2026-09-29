from django.urls import path
from . import views

app_name = 'club'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Admin
    path('tariffs/', views.tariffs_list, name='tariffs'),
    path('tariffs/new/', views.tariff_create, name='tariff_create'),
    path('tariffs/<int:pk>/edit/', views.tariff_edit, name='tariff_edit'),
    path('services/', views.services_list, name='services'),
    path('services/new/', views.service_create, name='service_create'),
    path('employees/', views.employees_list, name='employees'),
    path('employees/new/', views.employee_create, name='employee_create'),

    # Manager
    path('computers/', views.computers_list, name='computers'),
    path('computers/new/', views.computer_create, name='computer_create'),
    path('clients/', views.clients_list, name='clients'),
    path('clients/new/', views.client_create, name='client_create'),
    path('sessions/', views.sessions_list, name='sessions'),
    path('sessions/new/', views.session_create, name='session_create'),
]
