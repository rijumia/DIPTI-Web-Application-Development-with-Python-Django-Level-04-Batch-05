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
    
@api_view(['POST'])
def  addStudent(request):
    student_serializer = StudentSerializer(data=request.data)

    if student_serializer.is_valid():
        student_serializer.save()
        return Response({
            'success': True,
            'message': 'Student data create successfully.',
            'Create data': student_serializer.data
        },status=status.HTTP_201_CREATED)
    else:
        return Response({
            'success': False,
            'message': 'Invalid Operation.',
        },status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def deleteStudent(request, pk):
    student = StudentInfoModel.objects.get(pk=pk)
    student.delete()
    return Response({
        'success': True,
        'message': 'Student deleted successfully.'
    }, status=status.HTTP_200_OK)