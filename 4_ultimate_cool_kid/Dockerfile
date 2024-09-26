# Utilisation d'une image Python officielle comme base
FROM python:3.12-slim

# Installer Poetry
RUN pip install --no-cache-dir poetry

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY pyproject.toml poetry.lock /app/

# Installer les dépendances avec Poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copier le reste des fichiers dans le conteneur
COPY main.py /app/
COPY config.py /app/
COPY data/raw/client.csv /app/data/raw/client.csv

# Exporter la variable d'environnement VARVAR
ENV VARVAR="valeur_de_VARVAR"

# Exposer les paramètres de connexion à PostgreSQL via les variables d'environnement
ENV PG_HOST="localhost"
ENV PG_PORT="5432"
ENV PG_PASSWORD="mon_mot_de_passe"
ENV PG_DSN="postgresql://user:password@localhost/dbname"

# Commande pour exécuter le script Python
CMD ["python", "main.py"]
