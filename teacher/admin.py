from django.contrib import admin
from .models import Teacher, Subject, Section, Lesson, Homework, Submittion
# Register your models here.


admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(Homework)
admin.site.register(Submittion)
