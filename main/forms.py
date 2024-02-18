from django import forms
from .models import Call


class CallForm(forms.ModelForm):
    name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'input'}))
    phone = forms.CharField(label="Телефон",widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.CharField(label="Email",widget=forms.TextInput(attrs={'class': 'input'}))
    text = forms.CharField(label="Текс",widget=forms.TextInput(attrs={'class': 'textarea'}))
    class Meta:
        model = Call
        fields = ['name', 'phone', 'email', 'text']
