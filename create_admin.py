import os
import django

# Indiquer à Django où se trouve le fichier settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinique.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Vos identifiants de connexion pour le site
username = "admin"
password = "MonMotDePasse123!"
email = "admin@example.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print(f"--> Superutilisateur '{username}' créé avec succès !")
else:
    print(f"--> L'utilisateur '{username}' existe déjà.")