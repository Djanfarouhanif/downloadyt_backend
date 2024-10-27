import yt_dlp


# Fonction pour télécharger une vidoe Youtube
def download_video(url):
    ydl_opts = { 'format': 'best[ext=mp4]'}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print('Téléchargemment réussi avec yt-dlp !')

    except Exception as e:
        print(f"Erreur lors du téléchargemment avec yt-dlp: {e}")

url = 'https://youtu.be/9bZkp7q19f0'
download_video(url)