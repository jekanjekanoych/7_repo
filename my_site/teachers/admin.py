from django.contrib import admin

from teachers.models import Teacher


@admin.register(Teacher)
class PersonAdmin(admin.ModelAdmin):
    ordering = ["first_name"]
    list_filter = ["first_name", "last_name"]