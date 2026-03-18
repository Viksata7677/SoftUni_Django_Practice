from django.contrib import admin

from urls_and_views.departments.models import Department


# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass