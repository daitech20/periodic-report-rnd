from rest_framework import serializers
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


class PersonnelSerializer(serializers.ModelSerializer):
    time = serializers.CharField(source='time.time')
    class Meta:
        model = Personnel
        fields = '__all__'


class BugSerializer(serializers.ModelSerializer):
    time = serializers.CharField(source='time.time')
    project = serializers.CharField(source='project.name')
    assign_to = serializers.CharField(source='assign_to.username')
    status = serializers.CharField(source='status.name')

    class Meta:
        model = Bug
        fields = '__all__'


class ProjectReportSerializer(serializers.ModelSerializer):
    time = serializers.CharField(source='time.time')
    project = serializers.CharField(source='project.name')

    class Meta:
        model = ProjectReport
        fields = '__all__'


class NsnsSerializer(serializers.ModelSerializer):
    time = serializers.CharField(source='time.time')
    personnel = serializers.CharField(source='personnel.username')

    class Meta:
        model = Nsns
        fields = '__all__'


class KpiOkrSerializer(serializers.ModelSerializer):
    time = serializers.CharField(source='time.time')

    class Meta:
        model = KpiOkr
        fields = '__all__'


class EmergingIssuesSerializer(serializers.ModelSerializer):
    time = serializers.CharField(source='time.time')

    class Meta:
        model = EmergingIssues
        fields = '__all__'


class TimeOffSerializer(serializers.ModelSerializer):
    time = serializers.CharField(source='time.time')
    personnel = serializers.CharField(source='personnel.username')

    class Meta:
        model = TimeOff
        fields = '__all__'


class NextWeekPlanSerializer(serializers.ModelSerializer):
    time = serializers.CharField(source='time.time')

    class Meta:
        model = NextWeekPlan
        fields = '__all__'