from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import User
from .serializer import UserSerializer
# Create your views here.


class UserAPIView(APIView):
    permission_classes = [AllowAny]


    def get(self, request):
        user = User.objects.all()
        ser = UserSerializer(user, many=True)
        return Response(ser.data)


    def post(self, request):
        ser = UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


    def put(self, request, pk=None):
        if pk:
            user = User.objects.filter(pk=id).first()
            ser = UserSerializer(user, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
        return Response({"message": "user not found"})


    def delete(self, request, pk=None):
        if pk:
            user = User.objects.filter(pk=id).first()
            if user:
                user.delete()
                return Response({"message": "user deleted"})
        return Response({"message": "user not found"})