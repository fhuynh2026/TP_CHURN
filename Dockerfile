# Image de base
FROM python:3.12-slim

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers
COPY  requirements.txt requirements.txt
COPY app.py app.py
COPY data data
COPY templates templates

# Installer les dépendances

RUN pip install --no-cache-dir -r requirements.txt


# Exposer le port Flask
EXPOSE 5000

# Variables d'environnement (optionnel mais recommandé)

# Commande de lancement
CMD ["python", "app.py"]
