FROM python:3.9-slim

# Installation des dépendances système
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    ffmpeg \
    build-essential \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Mise à jour de pip
RUN pip install --no-cache-dir --upgrade pip

# Copie et installation des dépendances depuis requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code de l'application dans le conteneur
COPY . .

# Commande de démarrage par défaut
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
