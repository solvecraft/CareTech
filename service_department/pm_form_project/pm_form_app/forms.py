from django import forms
from .models import FormData
class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['model', 'sn', 'temperature']

