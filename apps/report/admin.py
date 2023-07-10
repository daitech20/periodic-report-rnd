from django.contrib import admin
from report.models import (
    Personnel,
    Bug,
    ProjectReport,
    Nsns,
    KpiOkr,
    EmergingIssues,
    TimeOff,
    NextWeekPlan
)
from django.utils.html import format_html
# Register your models here.


@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = (
        'time',
        'personnel_of_quota',
        'personnel_in',
        'personnel_out',
        'resignation_rate',
        'wfo_wfh',
        'health_status',
    )
    list_filter = ("time__time", )
    search_fields = ("time__time", )


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    def wrapped_modified(self, obj):
        return obj.modified.strftime('%Y-%m-%d')
    
    def wrapped_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')
    
    def wrapped_timeline(self, obj):
        return obj.timeline.strftime('%Y-%m-%d')
    
    wrapped_modified.short_description = 'modified'
    wrapped_created_at.short_description = 'created_at'
    wrapped_timeline.short_description = 'timeline'
    
    list_display = (
        'time',
        'project',
        'assign_to',
        'status',
        'id_bug',
        'wrapped_modified',
        'wrapped_created_at',
        'wrapped_timeline',
        'note',
    )
    list_filter = ("time__time", "timeline", "project__name", "status__name", "assign_to__username", )
    search_fields = ("time__time", "assign_to__username", )


@admin.register(ProjectReport)
class ProjectReportAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in ProjectReport._meta.get_fields()]
    def wrapped_feature(self, obj):
        return format_html('<br>'.join(obj.feature.splitlines()))

    def wrapped_overview(self, obj):
        return format_html('<br>'.join(obj.overview.splitlines()))

    def wrapped_bugs(self, obj):
        return format_html('<br>'.join(obj.bugs.splitlines()))
    
    def wrapped_plan(self, obj):
        return format_html('<br>'.join(obj.plan.splitlines()))

    def wrapped_emerging_issues(self, obj):
        return format_html('<br>'.join(obj.emerging_issues.splitlines()))

    def wrapped_pending_issues(self, obj):
        return format_html('<br>'.join(obj.pending_issues.splitlines()))
    
    wrapped_feature.short_description = 'feature'
    wrapped_bugs.short_description = 'bugs'
    wrapped_overview.short_description = 'overview'
    wrapped_plan.short_description = 'Kế hoạch tuần sau'
    wrapped_emerging_issues.short_description = 'Issue - Phát sinh'
    wrapped_pending_issues.short_description = 'Tồn đọng'

    list_display = (
        "time",
        "project",
        "wrapped_feature",
        "wrapped_overview",
        "wrapped_bugs",
        "wrapped_plan",
        "wrapped_emerging_issues",
        "wrapped_pending_issues",
    )
    list_filter = ("time__time", "project__name", )
    search_fields = ("time__time", "project__name",)


@admin.register(Nsns)
class NsnsAdmin(admin.ModelAdmin):
    list_display = (
        'time',
        'personnel',
        'nsns',
        'norm',
    )
    list_filter = ("time__time", "personnel__username",)
    search_fields = ("time__time", "personnel__username",)


@admin.register(KpiOkr)
class KpiOkrAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in KpiOkr._meta.get_fields()]

    def wrapped_docs(self, obj):
        return format_html('<br>'.join(obj.docs.splitlines()))
    
    def wrapped_update_taiga(self, obj):
        return format_html('<br>'.join(obj.update_taiga.splitlines()))
    
    def wrapped_reprimand(self, obj):
        return format_html('<br>'.join(obj.reprimand.splitlines()))
    
    def wrapped_seminar(self, obj):
        return format_html('<br>'.join(obj.seminar.splitlines()))
    
    def wrapped_certificate(self, obj):
        return format_html('<br>'.join(obj.certificate.splitlines()))
    
    def wrapped_stack_training(self, obj):
        return format_html('<br>'.join(obj.stack_training.splitlines()))
    
    def wrapped_bug_total(self, obj):
        return format_html('<br>'.join(obj.bug_total.splitlines()))

    wrapped_docs.short_description = 'Hoàn thành docs về tính năng - API (Flow, data schema, swimlane logic) trên mỗi task được nhận'
    wrapped_update_taiga.short_description = 'Hoàn thành update đủ thông tin task trên taiga'
    wrapped_reprimand.short_description = 'Đảm bảo số lần CBQL nhắc nhở, khiển trách về công việc, thái độ trách nhiệm của bản thân < 2 lần'
    wrapped_seminar.short_description = 'Nghiên cứu và trình bày seminar công nghệ'
    wrapped_certificate.short_description = 'Thi chứng chỉ quốc tế'
    wrapped_stack_training.short_description = 'Đào tạo stack'
    wrapped_bug_total.short_description = 'Có tổng số bug/sprint <= 5'

    list_display = (
        'time',
        'wrapped_docs',
        'wrapped_update_taiga',
        'wrapped_reprimand',
        'wrapped_seminar',
        'wrapped_certificate',
        'wrapped_stack_training',
        'wrapped_bug_total'
    )
    list_filter = ("time__time",)
    search_fields = ("time__time",)


@admin.register(EmergingIssues)
class EmergingIssuesAdmin(admin.ModelAdmin):
    def wrapped_team_meeting(self, obj):
        return format_html('<br>'.join(obj.team_meeting.splitlines()))
    
    def wrapped_review_new_personnel(self, obj):
        return format_html('<br>'.join(obj.review_new_personnel.splitlines()))
    
    def wrapped_employee_turnover(self, obj):
        return format_html('<br>'.join(obj.employee_turnover.splitlines()))
    
    def wrapped_hand_over_traning(self, obj):
        return format_html('<br>'.join(obj.hand_over_traning.splitlines()))
    
    def wrapped_movement(self, obj):
        return format_html('<br>'.join(obj.movement.splitlines()))
    
    wrapped_team_meeting.short_description = 'Họp team'
    wrapped_review_new_personnel.short_description = 'Đánh giá nhân sự mới'
    wrapped_employee_turnover.short_description = 'Biến động nhân sự'
    wrapped_hand_over_traning.short_description = 'Traning bàn giao'
    wrapped_movement.short_description = 'Phong trào'
    
    list_display = (
        'time',
        'wrapped_team_meeting',
        'wrapped_review_new_personnel',
        'wrapped_employee_turnover',
        'wrapped_hand_over_traning',
        'wrapped_movement',
    )
    list_filter = ("time__time", )
    search_fields = ("time__time",)


@admin.register(TimeOff)
class TimeOffAdmin(admin.ModelAdmin):
    list_display = (
        'time',
        'personnel',
        'timeoff_total',
        'timeoff_of_week',
        'reason',
    )
    list_filter = ("time__time", "personnel__username",)
    search_fields = ("time__time", "personnel__username",)


@admin.register(NextWeekPlan)
class NextWeekPlanAdmin(admin.ModelAdmin):
    def wrapped_plan(self, obj):
        return format_html('<br>'.join(obj.plan.splitlines()))
    
    wrapped_plan.short_description = 'Họp team'

    list_display = (
        'time',
        'wrapped_plan',
    )
    list_filter = ("time__time", )
    search_fields = ("time__time",)