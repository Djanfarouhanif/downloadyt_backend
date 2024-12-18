import yt_dlp


# Fonction pour télécharger une vidoe Youtube
def download_video(video_url, output_path='videos/%(title)s.%(ext)s'):
    print('"""""""""""""""""""""""""')
    ydl_opts = {
        'outtmpl': output_path, # Modéle de nom de fichier
        'format': 'bv+ba/b', # Sélectinner le meilleur format disponible
        'noplaylist': True, # Si c'est une playlist, on ne prend que la vidéo
        'quiet': False, # Afficher les logs pour plus de détails 
    }
    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)

            
            
            
            # Retourner le chemin du fichier et le titre
            file_path = ydl.prepare_filename(info_dict)
            
            return file_path # Retourne le chemin complet du fichier telecharge
    except yt_dlp.utils.DownloadError as e:
        print(f"Download erro: {e}")
        return None # Rétourner None en cas d'erreur de téléchargement
    except Exception as e :
        print(f"An unexpected error occured: {e}")
        return None # Retourner None en cas d'erreur inattendu

def videoData(video_url):
    ydl_opts = {
        'skip_download': True # Ne pas télécharger la video
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        
        # Récupére le titre de la video
        title = info_dict.get('title', 'Unknow Title')

        # Récupérer la miniature

        thumbnail = info_dict.get('thumbnail', 'No Thumbnail')

        return title , thumbnail




#--------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
# Fonction pour télécharger les audio
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best', #Télécharge uniquemment l'audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3', # Convertir en mp3
            'preferredquality': '192', # Qualité audio
        }],
        'outtmpl': '%(title)s.%(ext)s', # Nom de fichier basé sur le titre de la video
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print('Téléchargement audio réussi !')

# url = 'https://youtu.be/QQCTR11MSlc?si=u6iQkj6_3Pjc6kZM'
# download_audio(url)
#download_video(url)