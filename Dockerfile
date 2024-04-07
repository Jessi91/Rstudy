# Utiliser l'image Python officielle comme image de base
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app


# Copier le fichier des dépendances et installer les dépendances
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source de l'application dans le conteneur
COPY . /app/

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 8000

# # Commande pour démarrer l'application
# CMD ["python", "manage.py", "makemigrations"]


# Commande pour démarrer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
