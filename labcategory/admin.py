from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Labcategory


class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
admin.site.register(Labcategory, ProfileAdmin)

