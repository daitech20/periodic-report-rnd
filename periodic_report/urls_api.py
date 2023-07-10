from django.urls import include, path

report_urlpatterns = [
    path("report/", include("report.api.urls_api")),
]


urlpatterns = [
    *report_urlpatterns,
]