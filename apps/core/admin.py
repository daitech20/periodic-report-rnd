from django.contrib import admin
from core.models import Person, Project
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("username", "fullname", "position", )