from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from Youtube.main import download_video
from django.http import StreamingHttpResponse
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
            print("reussi")
            video_path = download_video(video_url)
          
            if not os.path.exists(video_path):
                print(f"Erreur: fichier {video_path} introuvable")
                return Response({"error": "Erreur de téléchargement du fichier."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
            # # Ouvre le ficher en mode de lecture binaire
            # with open(video_path, 'rb') as file_handle:
            #     # Crée une réponse de fichier pour envoyer le fichier au client
            #     response = FileResponse(file_handle, content_type='video/mp4')
            #     response['Content-Disposition'] = f'attachment; filename="{os.path.basename(video_path)}"'
            
            # Utilise StreamingHttpResponse pour le téléchargement
            def file_iterator(file_path,chunk_size=8192):
                try:
                    with open(file_path, 'rb') as f:
                        while chunk := f.read(chunk_size):
                            yield chunk
                except IOError as e:
                    print(f"Erreur lors de la lecture du fichier {e}")
            # Utilise StreamingHttpResponse pour le téléchargement
            response = StreamingHttpResponse(file_iterator(video_path), content_type='video/mp4')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(video_path)}"'

            #Fonction de rappel pour supprimer le fichier une fois la réponse terminée
           
            def cleanup_file(file_path):
                try:
                    os.remove(file_path)
                    print("Fichier supprimé aprés envoi")

                except OSError as e:
                    print(f"Erreur lors de la suppression du fichier : {e}")
            
            # Ajouter une fonction de nettoyage pour supprimer le fichier après l'envoye
            response['X-Sendfile'] = 'delete' # Ajoutez une en-tête pour que le serveur sache qu'il doit nettoyer 
            response.cleanup = cleanup_file # Liez la fonction de nettoyage à la reponse
            

            return response

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self, request, *args, **kwargs):
        #Retourne une réponse d'erreur pour les requête get
        return Response({"error": "Methode GET non autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)