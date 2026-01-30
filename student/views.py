from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Student
from .serializer import StudentSerializer
# Create your views here.


class StudentAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        student = Student.objects.all()
        ser = StudentSerializer(student, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def put(self, request, pk=None):
        if pk:
            student = Student.objects.filter(pk=id).first()
            ser = StudentSerializer(student, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
        return Response({"message": "student not found"})

    def delete(self, request, pk=None):
        if pk:
            student = Student.objects.filter(pk=id).first()
            if student:
                student.delete()
                return Response({"message": "student deleted"})
        return Response({"message": "student not found"})