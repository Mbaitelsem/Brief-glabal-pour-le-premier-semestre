from django import forms
from .models import task 

class Formtask(forms.ModelForm):
    tache = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Entrer votre tache',
        'class': 'form-control form-control-lg'
    }))


    class Meta:
        model = task 
        fields = [
            'tache',
        ]
