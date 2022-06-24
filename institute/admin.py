from django.contrib import admin

from institute.models import Institute
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class InstituteAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug':('institute_name',)}
    list_display = ('institute_name', 'slug')

admin.site.register(Institute, InstituteAdmin)