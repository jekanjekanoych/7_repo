from django.contrib import admin

from groups.models import Groups


@admin.register(Groups)
class PersonAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_filter = ["name"]
