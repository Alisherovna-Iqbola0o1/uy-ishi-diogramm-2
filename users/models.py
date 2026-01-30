from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.TextChoices):
    SUPER_ADMIN = "Super-admin", "Super-admin"
    ADMIN = "Admin", "Admin"
    TEACHER = "Teacher", "Teacher"
    STUDENT = "Student", "Student"
    SUPPORT_TEACHER = "Support-teacher", "Support-teacher"

class Gender(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0)
    birthday = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=Role.choices)
    is_active = models.BooleanField(default=True)
    language = models.CharField(max_length=3)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatars/")
    gender = models.CharField(max_length=10, choices=Gender.choices)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "phone_number"]

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"
