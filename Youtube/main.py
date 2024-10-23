from pytube import YouTube


#Fonction pour télécharger la video via l'URL de la video

def download_video(url):
    
    #Création d'un object YouTube
    yt = YouTube(url)

        # Sélection de la meilleure qualité vidéo disponible
    stream = yt.streams.get_highest_resolution()

    try: 
        #Téléchargement de la vidéo 
        
        stream.download()
        print('Téléchargement terminée !')

    except Exception as e :
        print(f' Errure lors de téléchargement : {e}')


url_video = input('urls') 

download_video(url_video)


