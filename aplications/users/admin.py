from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from aplications.users.models import *


@admin.register(Person)
class ViewAdmin(ImportExportModelAdmin):
    pass
