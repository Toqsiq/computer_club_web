from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Tariff, Service, Computer, Client, Club
from .forms import TariffForm, ServiceForm, ClientForm


def home(request):
    clubs = Club.objects.filter(is_active=True)
    tariffs_count = Tariff.objects.filter(is_active=True).count()
    services_count = Service.objects.filter(is_active=True).count()
    computers_count = Computer.objects.filter(is_active=True).count()

    return render(request, 'club/home.html', {
        'clubs': clubs,
        'tariffs_count': tariffs_count,
        'services_count': services_count,
        'computers_count': computers_count,
    })

# return render(...) Функция render берёт шаблон, подставляет в него данные и возвращает готовый HTTP-ответ (страницу)

def tariffs_list(request):
    tariffs = Tariff.objects.all().order_by('price')
    return render(request, 'club/tariffs.html', {'tariffs': tariffs})


def tariff_create(request):
    if request.method == 'POST':
        form = TariffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Тариф успешно добавлен!')
            return redirect('club:tariffs')
    else:
        form = TariffForm()
    return render(request, 'club/tariff_form.html', {'form': form, 'title': 'Новый тариф'})


def tariff_edit(request, pk):
    tariff = get_object_or_404(Tariff, pk=pk)
    if request.method == 'POST':
        form = TariffForm(request.POST, instance=tariff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Тариф обновлён!')
            return redirect('club:tariffs')
    else:
        form = TariffForm(instance=tariff)
    return render(request, 'club/tariff_form.html', {'form': form, 'title': 'Редактировать тариф'})


def services_list(request):
    services = Service.objects.all().order_by('name')
    return render(request, 'club/services.html', {'services': services})


def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Услуга успешно добавлена!')
            return redirect('club:services')
    else:
        form = ServiceForm()
    return render(request, 'club/service_form.html', {'form': form, 'title': 'Новая услуга'})


def computers_list(request):
    computers = Computer.objects.select_related('zone', 'status').filter(is_active=True)
    return render(request, 'club/computers.html', {'computers': computers})


def clients_list(request):
    clients = Client.objects.all().order_by('-registration_date')
    return render(request, 'club/clients.html', {'clients': clients})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Клиент добавлен!')
            return redirect('club:clients')
    else:
        form = ClientForm()
    return render(request, 'club/client_form.html', {'form': form, 'title': 'Новый клиент'})
