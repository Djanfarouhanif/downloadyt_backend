import yt_dlp


# Fonction pour télécharger une vidoe Youtube
def download_video(video_url, output_path='videos/%(title)s.%(ext)s'):
    print('"""""""""""""""""""""""""')
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        
        return ydl.prepare_filename(info_dict) # Retourne le chemin complet du fichier telecharge



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

# url = 'https://youtu.be/8hO7sdScJAM?si=Ggt1xlToY9HC8hrf'
# download_audio(url)
#download_video(url)