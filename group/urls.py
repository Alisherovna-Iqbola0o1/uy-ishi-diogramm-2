from django.urls import path
from .views import GroupAPIView

urlpatterns = [
    path('groups/', GroupAPIView.as_view(), name='group-list-create'),
    path('groups/<int:pk>/', GroupAPIView.as_view(), name='group-detail'),
]
