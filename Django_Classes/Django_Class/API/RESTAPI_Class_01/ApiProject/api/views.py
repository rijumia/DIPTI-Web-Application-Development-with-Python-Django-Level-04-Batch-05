from django.shortcuts import render
from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def studentList(request):
    if request.method == 'GET':
        student_data = StudentModel.objects.all()
        serializer = StudentSerializer(student_data, many=True)
        
        # return Response(serializer.data)
        return Response(
            {
                'success': True,
                'message': 'Student List successfully get.',
                'student_data': serializer.data,
            },status = status.HTTP_200_OK)
        
@api_view(['POST'])
def addStudent(request):
    student_serializar = StudentSerializer(data = request.data)
    if student_serializar.is_valid():
        student_serializar.save()
        return Response({
            'success': True,
            'message': 'Sudent Add Successfully.',
            'student_data': student_serializar.data,
        })
    else:
        return Response({
            'success': False,
            'message': 'Invalid Operation'
        })
        
        