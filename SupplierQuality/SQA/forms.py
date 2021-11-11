from typing_extensions import Required
from django import forms
from django.forms.widgets import Textarea
from .models import Supplier_T1

class Supplier_T1Form(forms.ModelForm):
    
    class Meta:
        model = Supplier_T1
        fields = ('name', 'address', 'valid_from', 'is_9001', 'is_17494')
