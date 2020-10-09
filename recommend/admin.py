from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ['date', 'state', 'province', 'name', 'type1', 'type2', 'type3', 'link']
    search_fields = ['state', 'province', 'name', 'type1', 'type2', 'type3']

admin.site.register(Data, DataAdmin)