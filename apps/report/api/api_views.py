from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from report.api.serializers import (
    PersonnelSerializer,
    BugSerializer,
    ProjectReportSerializer,
    NsnsSerializer,
    KpiOkrSerializer,
    EmergingIssuesSerializer,
    TimeOffSerializer,
    NextWeekPlanSerializer
)
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
from report.api.services import export_to_xlsx
from core.api.serializers import TimeLineSerializer
from core.models import TimeLine
from datetime import datetime
import io


class PersonnelList(generics.ListAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = ()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['time__time', 'time__title']


class BugList(generics.ListAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
    permission_classes = ()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['time__time', 'time__title', 'project__name', 'assign_to__username', 'status__name']


class ProjectReportList(generics.ListAPIView):
    queryset = ProjectReport.objects.all()
    serializer_class = ProjectReportSerializer
    permission_classes = ()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['time__time', 'time__title', 'project__name']


class NsnsList(generics.ListAPIView):
    queryset = Nsns.objects.all()
    serializer_class = NsnsSerializer
    permission_classes = ()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['time__time', 'time__title', 'personnel__username']
    filterset_fields = ['personnel__username',]


class KpiOkrList(generics.ListAPIView):
    queryset = KpiOkr.objects.all()
    serializer_class = KpiOkrSerializer
    permission_classes = ()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['time__time', 'time__title']


class EmergingIssuesList(generics.ListAPIView):
    queryset = EmergingIssues.objects.all()
    serializer_class = EmergingIssuesSerializer
    permission_classes = ()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['time__time', 'time__title']


class TimeOffList(generics.ListAPIView):
    queryset = TimeOff.objects.all()
    serializer_class = TimeOffSerializer
    permission_classes = ()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['time__time', 'time__title', 'personnel__username']


class NextWeekPlanList(generics.ListAPIView):
    queryset = NextWeekPlan.objects.all()
    serializer_class = NextWeekPlanSerializer
    permission_classes = ()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['time__time', 'time__title']


class ExportReportView(APIView):
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        # try:
        #     date_str = request.GET['time']
        #     date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
        #     timeline = TimeLine.objects.get(time=date_object)
        #     response = HttpResponse(content_type='application/ms-excel')
        #     response['Content-Disposition'] = f'attachment; filename="Report {str(timeline)}.xls"'
        #     ws = export_to_xlsx(timeline)
        #     ws.save(response)

        # except:
        #     return Response({"error": "not found"}, status=status.HTTP_400_BAD_REQUEST)

        # return response
        date_str = request.GET['time']
        date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
        timeline = TimeLine.objects.get(time=date_object)
        output = io.BytesIO()
        
        export_to_xlsx(timeline, output)
        output.seek(0)

        response = HttpResponse(
            output,
            content_type='application/ms-excel'
        )
        response['Content-Disposition'] = f'attachment; filename="Report {str(date_object)}.xlsx"'

        return response