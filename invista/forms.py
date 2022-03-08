from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Investimento

class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__'
        #mostra todos