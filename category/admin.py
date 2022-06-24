from django.contrib import admin
from .models import Category
# Register your models here.
from import_export.admin import ImportExportModelAdmin

class CategoryAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')
admin.site.register(Category, CategoryAdmin)