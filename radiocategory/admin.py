from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Radcategory


class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
admin.site.register(Radcategory, ProfileAdmin)

