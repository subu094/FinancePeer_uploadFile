from django.contrib import admin
from .models import JsonDatas
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# @admin.register(Person)
# class PersonAdmin(ImportExportModelAdmin):
#     list_display= ('name', 'email', 'location')

@admin.register(JsonDatas)
class JsonDataAdmin(ImportExportModelAdmin):
    list_display= ('userId', 'title', 'body')