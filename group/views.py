from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Group
from .serializer import GroupSerializer


class GroupAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk=None):
        if pk is None:
            return Response({"message": "Please provide group id"}, status=400)
        group = Group.objects.filter(id=pk).first()
        if not group:
            return Response({"message": "Group not found"}, status=404)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"message": "Please provide group id"}, status=400)
        group = Group.objects.filter(id=pk).first()
        if not group:
            return Response({"message": "Group not found"}, status=404)
        group.delete()
        return Response({"message": "Group deleted"})
