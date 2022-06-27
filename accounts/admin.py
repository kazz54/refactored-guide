from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import User



class labAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
admin.site.register(User, labAdmin)

