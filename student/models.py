from django.db import models
from users.models import User

class Student(models.Model):

    class StudentStatus(models.TextChoices):
        YANGI = "yangi"
        OQIMOQDA = "oqimoqda"
        TUGATGAN = "tugatgan"
        CHIQIB_KETGAN = "chiqib ketgan"
        CHETLASHTIRILGAN = "chetlashtirilgan"

    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="students")
    status = models.CharField(
        max_length=20,
        choices=StudentStatus.choices,
        default=StudentStatus.YANGI
    )
    coin = models.IntegerField(default=0)
    wallet = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.status}"


class StudentAttandanceStatus(models.TextChoices):
    HERE = "here"
    ABSENT = "kelmagan"
    CAUSE_ABSENT = "cause_absent"


class StudentAttandance(models.Model):
    group = models.ForeignKey('group.Group', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey('teacher.Subject', on_delete=models.SET_NULL, null=True)
    student_status = models.CharField(
        max_length=20,
        choices=StudentAttandanceStatus.choices,
        default=StudentAttandanceStatus.ABSENT
    )
    date = models.DateField(blank=True, null=True)
    ball = models.PositiveIntegerField(default=0)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Group: {self.group}, Teacher: {self.teacher}, Student: {self.student_status}"
