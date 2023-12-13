FROM python:3.8

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie l'ensemble du projet dans le conteneur
COPY . /app/

# Expose le port sur lequel votre application va s'exécuter
EXPOSE 8000

# Commande pour démarrer votre application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
