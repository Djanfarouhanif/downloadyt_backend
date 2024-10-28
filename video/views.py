from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from Youtube.main import download_video
from django.http import FileResponse
import os

# Create your views here.

class VideoDownloadView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        video_url = request.data.get('video_url')

        if not video_url :
            return Response({"error": "URL de la vidéo manquante"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Télécharger la vidéo et récupére le chemin du fichier
            video_path = download_video(video_url)
            
            # Ouvre le ficher en mode de lecture binaire
            file_handle = open(video_path, 'rb')

            # Crée une réponse de fichier pour envoyer le fichier au client
            response = FileResponse(file_handle,content_type='video/mp4')
            response['Content-Dispositon'] = f'attachment; filename="{os.path.basename(video_path)}"'
            
            # Optionnel : Supprimer le fichier après envoi
            os.remove(video_path)

            return response

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        