from django.db import models
from users.models import User
from student.models import Student

class TeacherChoices(models.TextChoices):
    ISHLAYAPTI = "ishlayapti"
    ISHDAN_CHIQIB_KETGAN = "ishdan_chiqib_ketgan"
    TATILDA = "tatilda"
    DEKRETDA = "dekretda"
    CHETLASHTIRILGAN = "chetlashtirilgan"

class Subject(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.name_uz} - {self.name_ru} {self.image}"

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="teacher")
    salary = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=TeacherChoices.choices,
        default=TeacherChoices.ISHLAYAPTI
    )
    is_support = models.BooleanField(default=False)
    subject = models.ForeignKey('Subject', on_delete=models.RESTRICT, related_name="subjects")
    expirience = models.IntegerField(default=0)

    def __str__(self):
        return f"Teacher:{self.user}, {self.status} - {self.salary}"

class Section(models.Model):
    subjects = models.ForeignKey('Subject', on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    desc_uz = models.TextField(blank=True, null=True)
    desc_ru = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.subjects}, {self.is_active} - {self.order}"

class Lesson(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    desc_uz = models.TextField(blank=True, null=True)
    desc_ru = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)
    image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.section}, {self.order} - {self.file}"

class Homework(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='homeworks')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='homeworks')
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    desc_uz = models.TextField(blank=True, null=True)
    desc_ru = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)
    image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.lesson} - {self.name_uz} by {self.teacher}"

class Submittion(models.Model):
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    ball = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.teacher}, {self.student} - {self.ball}"
