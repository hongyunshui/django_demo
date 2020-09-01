from django import forms
from .models import NaturalPerson


class NaturalPersonForm(forms.ModelForm):
    class Meta:
        model = NaturalPerson
        fields = ['name', 'sex', 'nation', 'id', 'addr', 'sio']
        # labels = {'name': '', 'sex': '', 'nation': '', 'id': '', 'addr': '', 'sio': ''}
