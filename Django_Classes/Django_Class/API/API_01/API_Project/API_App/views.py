from django.shortcuts import render
from API_App.models import *
from API_App.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def studentList(request):
    if request.method == 'GET':
        student_data = StudentInfoModel.objects.all()
        serializer = StudentSerializer(student_data, many=True)
        # return Response(serializer.data)

        return Response({
            'success': True,
            'message': 'Student Information List Get.',
            'Student Data': serializer.data
        },status=status.HTTP_200_OK)