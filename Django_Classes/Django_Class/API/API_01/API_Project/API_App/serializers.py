from rest_framework import serializers
from API_App.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfoModel
        fields = '__all__'

