from django.urls import include, path
from report.api.api_views import (
    PersonnelList,
    BugList,
    ProjectReportList,
    NsnsList,
    KpiOkrList,
    EmergingIssuesList,
    TimeOffList,
    NextWeekPlanList,
    ExportReportView
)


urlpatterns = [
    path('personnels', PersonnelList.as_view()),
    path('bugs', BugList.as_view()),
    path('project-reports', ProjectReportList.as_view()),
    path('nsns', NsnsList.as_view()),
    path('kpi-okr', KpiOkrList.as_view()),
    path('emerging-issues', EmergingIssuesList.as_view()),
    path('timeoff', TimeOffList.as_view()),
    path('nextweek-plan', NextWeekPlanList.as_view()),
    path('export', ExportReportView.as_view()),

]