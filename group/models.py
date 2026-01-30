from django.db import models
from teacher.models import Subject, Teacher
from student.models import Student

class Week(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

class Room(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(default=1)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name_uz} Room - Number-{self.number}"

class Group(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name="groups")
    is_active = models.BooleanField(default=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT, related_name="groups")
    students = models.ManyToManyField(Student, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name_uz}, Teacher: {self.teacher}, Subject: {self.subject}"
