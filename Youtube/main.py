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

        # Récupérer le titre de la vidéo
        title = info_dict.get('title', 'Unknow Title')

        # Retourner le chemin du fichier et le titre
        file_path = ydl.prepare_filename(info_dict)
        
        return file_path, title # Retourne le chemin complet du fichier telecharge



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

# url = ''
# download_audio(url)
#download_video(url)