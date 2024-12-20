# Utilisation de l'image Python de base 
FROM python:3.10-slim 

# Mise à jour et installation de FFmpeg 
RUN apt-get update && \ 
             apt-get install -y \
            apt-utils \
            ffmpeg  \ 
            && rm -rf /var/lib/apt/lists/*

# Répertoire de travail 

WORKDIR /app 

# Copieer les fichiers de mon projet 
COPY . /app
 
# Installation des dépendances  

RUN pip install --no-cache-dir -r requirements.txt 
 
# Exposer le port sur lequel mon application va tourner  

EXPOSE 8000 

# Commande pour démarrer l"application 

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]