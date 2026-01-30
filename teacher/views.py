from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Teacher, Subject, Section, Lesson, Homework, Submittion
from .serializer import TeacherSerializer, SubjectSerializer, SectionSerializer, LessonSerializer, HomeworkSerializer, SubmittionSerializer

# Create your views here.


class TeacherAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        teachers = Teacher.objects.all()
        ser = TeacherSerializer(teachers, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = TeacherSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def put(self, request, pk=None):
        if pk:
            teacher = Teacher.objects.filter(id=pk).first()
            ser = TeacherSerializer(teacher, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
        return Response({"message": "teacher not found"})

    def delete(self, request, pk=None):
        if pk:
            teacher = Teacher.objects.filter(id=pk).first()
            if teacher:
                teacher.delete()
                return Response({"message": "deleted"})
        return Response({"message": "teacher not found"})


class SubjectAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        subjects = Subject.objects.all()
        ser = SubjectSerializer(subjects, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = SubjectSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def put(self, request, pk=None):
        if pk:
            subject = Subject.objects.filter(id=pk).first()
            ser = SubjectSerializer(subject, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
        return Response({"message": "subject not found"})

    def delete(self, request, pk=None):
        if pk:
            subject = Subject.objects.filter(id=pk).first()
            if subject:
                subject.delete()
                return Response({"message": "deleted"})
        return Response({"message": "subject not found"})


class SectionAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        sections = Section.objects.all()
        ser = SectionSerializer(sections, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = SectionSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def put(self, request, pk=None):
        if pk:
            section = Section.objects.filter(id=pk).first()
            ser = SectionSerializer(section, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
        return Response({"message": "section not found"})

    def delete(self, request, pk=None):
        if pk:
            section = Section.objects.filter(id=pk).first()
            if section:
                section.delete()
                return Response({"message": "deleted"})
        return Response({"message": "section not found"})


class LessonAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        lessons = Lesson.objects.all()
        ser = LessonSerializer(lessons, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = LessonSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def put(self, request, pk=None):
        if pk:
            lesson = Lesson.objects.filter(id=pk).first()
            ser = LessonSerializer(lesson, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
        return Response({"message": "lesson not found"})

    def delete(self, request, pk=None):
        if pk:
            lesson = Lesson.objects.filter(id=pk).first()
            if lesson:
                lesson.delete()
                return Response({"message": "deleted"})
        return Response({"message": "lesson not found"})


class HomeworkAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        homeworks = Homework.objects.all()
        ser = HomeworkSerializer(homeworks, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = HomeworkSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def put(self, request, pk=None):
        if pk:
            homework = Homework.objects.filter(id=pk).first()
            ser = HomeworkSerializer(homework, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
        return Response({"message": "homework not found"})

    def delete(self, request, pk=None):
        if pk:
            homework = Homework.objects.filter(id=pk).first()
            if homework:
                homework.delete()
                return Response({"message": "deleted"})
        return Response({"message": "homework not found"})


class SubmittionAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        submissions = Submittion.objects.all()
        ser = SubmittionSerializer(submissions, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = SubmittionSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def put(self, request, pk=None):
        if pk:
            submission = Submittion.objects.filter(id=pk).first()
            ser = SubmittionSerializer(submission, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
        return Response({"message": "submission not found"})

    def delete(self, request, pk=None):
        if pk:
            submission = Submittion.objects.filter(id=pk).first()
            if submission:
                submission.delete()
                return Response({"message": "deleted"})
        return Response({"message": "submission not found"})
