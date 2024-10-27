from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from Youtube.main import download_video
# Create your views here.

class VideoDownloadView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        video_url = request.data.get('video_url')

        if not video_url :
            return Response({"error": "URL de la vidéo manquante"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Appel de la fonction existante
            video_title = download_video(video_url)
            return Response({"message": f"La vidéo '{video_title}' a été taléchargée avec success"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        