from django.contrib import admin
from core.models import (
    BugStatus,
    Employee,
    Project,
    TimeLine
)
# Register your models here.
@admin.register(BugStatus)
class BugStatus(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("username", "fullname", "position", )


@admin.register(TimeLine)
class TimeLineAdmin(admin.ModelAdmin):
    list_display = ("title", "time", )
    list_filter = ("time", )