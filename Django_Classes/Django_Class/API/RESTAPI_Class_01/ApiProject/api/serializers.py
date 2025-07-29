from rest_framework import serializers
from api.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        
        fields = '__all__'
    
    def create(self, validated_data):
        student_name = validated_data.get('studentName')
        student = StudentModel.objects.order_by('-studentRoll').first()
    
        if student:
            roll = student.studentRoll + 1
        else:
            roll = 1
        instance_data = StudentModel.objects.create(**validated_data)
        instance_data.studentRoll = roll
        instance_data.studentUsername = student_name + str(roll)
        instance_data.save()
        return instance_data