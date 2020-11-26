from django import forms
from .models import NaturalPerson, Enterprise
# from .mysql_view_models import MysqlViewTest


class NaturalPersonForm(forms.ModelForm):
    class Meta:
        model = NaturalPerson
        fields = ['name', 'sex', 'nation', 'id', 'addr', 'sio']
        # labels = {'name': '', 'sex': '', 'nation': '', 'id': '', 'addr': '', 'sio': ''}


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['id',  'adm', 'name', 'addr', 'registration_authority']

    # def __init__(self, *args, **kwargs, ):
    #     self.request = kwargs.pop("request")
    #     enterprise_adm = self.request.Enterprise.adm.site.id
    #     super(EnterpriseForm, self).__init__(*args, **kwargs, )
    #     if 'instance' in kwargs.keys():
    #         print(kwargs['instance'])
    #         self.fields['adm'].disabled = True
    #         self.fields['NaturalPerson'].queryset = NaturalPerson.objects.filter(Q(np_id = self.instance.id))


 
# class MysqlViewModelsForm(forms.ModelForm):
#     class Meta:
#         model = MysqlViewTest
#         fields = ['name', 'addr', 'id', 'stove_id']

