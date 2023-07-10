from django.db import models
from django.utils import timezone
from core.models import (
    BugStatus,
    Project,
    Employee,
    TimeLine
)

# Create your models here.
# BUG_STATUS = (
#     (0, "New"),
#     (1, "In process"),
#     (2, "Ready for test"),
#     (3, "Ready for stg"),
#     (4, "Ready at dev"),
#     (5, "Stg ok"),
#     (6, "Ready for STG(STG)"),
#     (7, "Ready for test(STG)"),
#     (8, "Reopen"),
#     (9, "Close")
# )

class Personnel(models.Model):
    time = models.ForeignKey(TimeLine, on_delete=models.CASCADE, verbose_name="Thời gian")
    personnel_of_quota = models.CharField(max_length=50, verbose_name="Tổng CBNV / quota")
    personnel_in = models.IntegerField(default=0, verbose_name="Số nhân sự in")
    personnel_out = models.IntegerField(default=0, verbose_name="Số nhân sự out")
    resignation_rate = models.IntegerField(default=0, verbose_name="Tỉ lệ nghỉ việc <20% (2NS/1NĂM)")
    wfo_wfh = models.CharField(max_length=10, verbose_name="WFO-WFH")
    health_status = models.CharField(max_length=100, default="Bình thường", verbose_name="Tình hình sức khỏe")

    class Meta:
        verbose_name_plural = "Nhân sự"


class Bug(models.Model):
    time = models.ForeignKey(TimeLine, on_delete=models.CASCADE, verbose_name="Thời gian")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="bugs_project", verbose_name="Dự án")
    assign_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="bugs_assign_to", verbose_name="Assign to")
    status = models.ForeignKey(BugStatus, on_delete=models.CASCADE, related_name="bugs_status")
    id_bug = models.CharField(max_length=10)
    modified = models.DateField(default=timezone.now)
    created_at = models.DateField(default=timezone.now)
    timeline = models.DateField(default=timezone.now, null=True)
    note = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name_plural = "Số bugs"
    

class ProjectReport(models.Model):
    time = models.ForeignKey(TimeLine, on_delete=models.CASCADE, verbose_name="Thời gian")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_reports", verbose_name="Dự án")
    overview = models.TextField(verbose_name="Over view")
    feature = models.TextField(verbose_name="Tính năng")
    bugs = models.TextField(verbose_name="Bugs")
    plan = models.TextField(verbose_name="Kế hoạch tuần sau")
    emerging_issues = models.TextField(verbose_name="Issue - Phát sinh")
    pending_issues = models.TextField(verbose_name="Tồn đọng")

    class Meta:
        unique_together = ('time', 'project', )
        verbose_name_plural = "Dự án"


class Nsns(models.Model):
    time = models.ForeignKey(TimeLine, on_delete=models.CASCADE, verbose_name="NSNS")
    personnel = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Nhân sự")
    nsns = models.IntegerField(default=0)
    norm = models.IntegerField(default=0, verbose_name="% norm tuần")

    class Meta:
        unique_together = ('time', 'personnel', )
        verbose_name_plural = "Năng suất nhân sự"


class KpiOkr(models.Model):
    time = models.OneToOneField(TimeLine, on_delete=models.CASCADE, verbose_name="Thời gian")
    docs = models.TextField(verbose_name="Hoàn thành docs về tính năng - API (Flow, data schema, swimlane logic) trên mỗi task được nhận")
    update_taiga = models.TextField(verbose_name="Hoàn thành update đủ thông tin task trên taiga ")
    bug_total = models.TextField(verbose_name="Có tổng số bug/sprint <= 5")
    reprimand = models.TextField(verbose_name="Đảm bảo số lần CBQL nhắc nhở, khiển trách về công việc, thái độ trách nhiệm của bản thân < 2 lần")
    seminar = models.TextField(verbose_name="Nghiên cứu và trình bày seminar công nghệ")
    certificate = models.TextField(verbose_name="Thi chứng chỉ quốc tế")
    stack_training = models.TextField(verbose_name="Đào tạo stack")
    
    class Meta:
        verbose_name_plural = "KPI & OKR"


class EmergingIssues(models.Model):
    time = models.OneToOneField(TimeLine, on_delete=models.CASCADE, verbose_name="Thời gian")
    team_meeting = models.TextField(verbose_name="Họp team")
    review_new_personnel = models.TextField(verbose_name="Đánh giá nhân sự mới")
    employee_turnover = models.TextField(verbose_name="Biến động nhân sự")
    hand_over_traning = models.TextField(verbose_name="Traning bàn giao") 
    movement = models.TextField(verbose_name="Phong trào")

    class Meta:
        verbose_name_plural = "Vấn đề phát sinh"


class TimeOff(models.Model):
    time = models.ForeignKey(TimeLine, on_delete=models.CASCADE, verbose_name="Thời gian")
    personnel = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Nhân sự")
    timeoff_total = models.FloatField(default=0, verbose_name="số ngày phép đã nghỉ")
    timeoff_of_week = models.FloatField(default=0, verbose_name="số ngày nghỉ trong tuần")
    reason = models.CharField(max_length=50, verbose_name="lý do")

    class Meta:
        unique_together = ('time', 'personnel', )
        verbose_name_plural = "Nghỉ phép"


class NextWeekPlan(models.Model):
    time = models.OneToOneField(TimeLine, on_delete=models.CASCADE, verbose_name="Thời gian")
    plan = models.TextField(verbose_name="Kế hoạch")

    class Meta:
        verbose_name_plural = "Kế hoạch tuần tới"