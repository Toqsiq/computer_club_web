from django import forms
from .models import Tariff, Service, Client


class TariffForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = ['name', 'duration_minutes', 'price', 'description', 'is_active']
        labels = {
            'name': 'Название',
            'duration_minutes': 'Длительность (минуты)',
            'price': 'Цена (₽)',
            'description': 'Описание',
            'is_active': 'Активен',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'form-input', 'min': 1}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01', 'min': 0}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price', 'description', 'is_active']
        labels = {
            'name': 'Название',
            'price': 'Цена (₽)',
            'description': 'Описание',
            'is_active': 'Активна',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01', 'min': 0}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check'}),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'phone', 'email']
        labels = {
            'full_name': 'ФИО',
            'phone': 'Телефон',
            'email': 'Email',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+7 (999) 123-45-67'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }
