from django.urls import path
from .views import TeacherAPIView, SubjectAPIView, SectionAPIView, LessonAPIView, HomeworkAPIView, SubmittionAPIView

urlpatterns = [
    path('teachers/', TeacherAPIView.as_view()),
    path('teachers/<int:pk>/', TeacherAPIView.as_view()),

    path('subjects/', SubjectAPIView.as_view()),
    path('subjects/<int:pk>/', SubjectAPIView.as_view()),

    path('sections/', SectionAPIView.as_view()),
    path('sections/<int:pk>/', SectionAPIView.as_view()),

    path('lessons/', LessonAPIView.as_view()),
    path('lessons/<int:pk>/', LessonAPIView.as_view()),

    path('homeworks/', HomeworkAPIView.as_view()),
    path('homeworks/<int:pk>/', HomeworkAPIView.as_view()),

    path('submissions/', SubmittionAPIView.as_view()),
    path('submissions/<int:pk>/', SubmittionAPIView.as_view()),
]
