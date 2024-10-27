from django.urls import path
from .views import VideoDownloadView



urlpatterns = [
    path('download-video/', VideoDownloadView.as_view(), name='download-video')
]