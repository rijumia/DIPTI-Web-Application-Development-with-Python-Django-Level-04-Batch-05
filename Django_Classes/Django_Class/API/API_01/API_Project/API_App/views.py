from django.shortcuts import render
from API_App.models import *
from API_App.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

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
    
@api_view(['PUT'])
def updateStudent(request, pk):
    student = StudentInfoModel.objects.get(id=pk)
    student_serializer = StudentSerializer(student, data = request.data, partial=True)
    if student_serializer.is_valid():
        student_serializer.save()
        return Response(student_serializer.data)
    else:
        return Response(student_serializer.errors)

@api_view(['DELETE'])
def deleteStudent(request, pk):
    student = StudentInfoModel.objects.get(pk=pk)
    student.delete()
    return Response({
        'success': True,
        'message': 'Student deleted successfully.'
    }, status=status.HTTP_200_OK)
    
class TeacherAPIView(APIView):
    def get(self, request):
        teacher_data = TeacherModel.objects.all()
        
        serializer = TeacherSerializer(teacher_data, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

class TeacherDetails(APIView):

    def put(self, request, pk):
        try:
            teacher = TeacherModel.objects.get(id=pk)
        except TeacherModel.DoesNotExist:
            return Response({'message': 'Teacher does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Teacher data updated successfully.',
                'teacher_data': serializer.data,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            teacher = TeacherModel.objects.get(id=pk)
        except TeacherModel.DoesNotExist:
            return Response({'message': 'Teacher does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        teacher.delete()
        return Response({'message': 'Teacher deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class TeacherViewSet(ModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer