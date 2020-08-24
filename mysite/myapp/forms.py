from django import forms
from django.forms import ModelForm
from .models import Empresa

class MyForm(ModelForm):
    nome_da_empresa = forms.CharField(label='Nome da Empresa', widget= forms.TextInput(attrs={'class': 'form-control '}))
    demanda_contratada = forms.CharField(label='Demanda Contratada', widget= forms.TextInput(attrs={'class': 'form-control '}))
    demanda_registrada = forms.CharField(label='Demanda Registrada', widget= forms.TextInput(attrs={'class': 'form-control '}))
    demanda_contratada = forms.CharField(label='Demanda Contratada', widget= forms.TextInput(attrs={'class': 'form-control '}))
    consumo_ponta = forms.CharField(label='Consumo em Ponta', widget= forms.TextInput(attrs={'class': 'form-control '}))
    consumo_Fora_ponta = forms.CharField(label='Consumo Fora de Ponta', widget= forms.TextInput(attrs={'class': 'form-control '}))

    class Meta:
        model = Empresa
        fields = ['nome_da_empresa', 'demanda_contratada', 'demanda_registrada', 
        'consumo_ponta', 'consumo_Fora_ponta']