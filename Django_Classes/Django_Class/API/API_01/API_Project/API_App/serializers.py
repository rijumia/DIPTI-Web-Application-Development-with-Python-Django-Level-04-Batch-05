from rest_framework import serializers
from API_App.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfoModel
        fields = '__all__'

    def create(self, validated_data):
        student_name = validated_data.get('StudentName') or ""

        latest_student = StudentInfoModel.objects.order_by('-StudentRoll').first()
        if latest_student and latest_student.StudentRoll:
            roll = latest_student.StudentRoll + 1
        else:
            roll = 1

        student_data = StudentInfoModel.objects.create(
            StudentRoll=roll,
            StudentUsername=student_name + str(roll),
            StudentName=validated_data.get('StudentName'),
            StudentAge=validated_data.get('StudentAge'),
            )
        return student_data
    
    
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'

