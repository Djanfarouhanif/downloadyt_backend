from pytube import YouTube


#Fonction pour télécharger la video via l'URL de la video

def  download_video(url):
    try:
        yt = YouTube(url)
        print("terminé")
    except :
        print("erreur")


url = "https://youtu.be/w8PVpWxE5_8?si=Q2eijSN3-ni-zwV-"
download_video(url)