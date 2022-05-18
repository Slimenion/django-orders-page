from .models import Orders
from django.forms import ModelForm, TextInput, EmailInput, Select


class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = ["customers_name", "email", "product", "service"]
        widgets = {
            "customers_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше ФИО'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control mt-4',
                'placeholder': 'Введите ваш email'
            }),
            "product": Select(attrs={
                'class': 'form-select mt-4',
                'aria-label': "Default select example"
            }),
            "service": Select(attrs={
                'class': 'form-select mt-4',
                'aria-label': "Default select example"
            }),
        }