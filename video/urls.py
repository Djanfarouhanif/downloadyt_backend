from django.urls import path
from .views import VideoDownloadView, VideoDataView



urlpatterns = [
    path('download-video/', VideoDownloadView.as_view(), name='download-video'),
    path('video-data/', VideoDataView.as_view(), name='video-data')

]