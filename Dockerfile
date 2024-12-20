FROM python:3.9-slim

# Installation des dépendances système avec les flags recommandés
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    ffmpeg \
    build-essential \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Mise à jour de pip en tant que root avec --no-cache-dir
RUN pip install --no-cache-dir --upgrade pip

# Copie et installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000