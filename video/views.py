from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from Youtube.main import download_video, videoData
from django.http import StreamingHttpResponse, FileResponse
import os

# Create your views here.

class VideoDownloadView(APIView):
    parser_classes = [JSONParser]

    def get(self, request):
        
        video_url = request.data.get('video_url')
        

        if not video_url :
            return Response({"error": "URL de la vidéo manquante"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Télécharger la vidéo et récupére le chemin du fichier
          
            
            video_path = download_video(video_url)
            
            #video_path = '../videos/Gazo - PROBATION.mp4'
            if not os.path.exists(video_path):
                print(f"Erreur: fichier {video_path} introuvable")
                return Response({"error": "Erreur de téléchargement du fichier."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
            # # Ouvre le ficher en mode de lecture binaire
            # with open(video_path, 'rb') as file_handle:
            #     # Crée une réponse de fichier pour envoyer le fichier au client
            #     response = FileResponse(file_handle, content_type='video/mp4')
            #     response['Content-Disposition'] = f'attachment; filename="{os.path.basename(video_path)}"'
            
            # Utilise StreamingHttpResponse pour le téléchargement
            response = FileResponse(open(video_path, 'rb'), content_type='video/mp4')
            response['Content-Disposition'] =  f'attachment; filename="video.mp4"'
            response['X-Sendfile'] = 'delete' # En-tête pour indiquer que le fichier doit être suprimer
            # Ajouter la fonction de nettoyage
            response.cleanup = lambda: os.remove(video_path)

            return response

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class VideoDataView(APIView):
    parser_classes = [JSONParser]
    def get(self, request):
        video_url = request.data.get('video_url')

        if not video_url:
            return Response({"erreur": "L'URL de la video manque"}, stauts=status.HTTP_400_BAD_REQUEST)

        try:
            # Télécharger les informations de la video

            video_data = videoData(video_url)

            title = video_data[0]
            thumbnail = video_data[1]

            data = { 
                'title': title,
                'Thumbnail': thumbnail
            }

            return Response({'success': data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            


        

            

