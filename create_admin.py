import os
import sys
import django

# Indiquer à Python d'inclure le sous-dossier 'clinique'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'clinique'))

# Configuration des paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinique.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Identifiants du compte administrateur
username = "admin"
password = "MonMotDePasse123!"
email = "admin@example.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print(f"--> Superutilisateur '{username}' créé avec succès !")
else:
    print(f"--> L'utilisateur '{username}' existe déjà.")