# 1. Image de base
FROM python:3.11-slim

# 2. Créer un répertoire app
WORKDIR /app

# 3. Copier requirements
COPY requirements.txt .

# 4. Installer dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier tout le projet
COPY . .

# 6. Exposer un port si nécessaire (pas obligatoire ici pour batch)
EXPOSE 8080

# 7. Définir la commande par défaut (tu peux changer selon le script à exécuter)
CMD ["python", "src/embeddings/script.py"]
