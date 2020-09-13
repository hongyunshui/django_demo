from django.contrib import admin
from .models import NaturalPerson, RecordsSource, BaseRecordsTB

# Register your models here.
admin.site.register(NaturalPerson)
admin.site.register(BaseRecordsTB)
admin.site.register(RecordsSource)


