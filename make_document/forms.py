from django import forms
from .models import NaturalPerson
# from .mysql_view_models import MysqlViewTest


class NaturalPersonForm(forms.ModelForm):
    class Meta:
        model = NaturalPerson
        fields = ['name', 'sex', 'nation', 'id', 'addr', 'sio']
        # labels = {'name': '', 'sex': '', 'nation': '', 'id': '', 'addr': '', 'sio': ''}

 
# class MysqlViewModelsForm(forms.ModelForm):
#     class Meta:
#         model = MysqlViewTest
#         fields = ['name', 'addr', 'id', 'stove_id']

