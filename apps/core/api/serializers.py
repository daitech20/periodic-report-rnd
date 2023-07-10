from core.models import TimeLine
from rest_framework import serializers



class TimeLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeLine
        fields = ['time']