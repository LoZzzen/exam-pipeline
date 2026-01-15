# Image de base imposée
FROM python:3.11-slim-bookworm

# Dossier de travail
WORKDIR /app

# On copie et installe les dépendances d'abord
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# CORRECTION : On copie tout le contenu d'examen-final (app.py, etc.)
COPY . .

# Port pour Flask
EXPOSE 5000

# Lancement de l'application
CMD ["python", "app.py"]
