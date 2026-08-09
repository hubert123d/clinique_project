"""
WSGI config for clinique project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinique.settings')

application = get_wsgi_application()

# Création automatique du compte administrateur au démarrage du serveur Render
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'MonMotDePasse123!')
        print("--> Compte administrateur 'admin' créé avec succès !")
except Exception as e:
    print(f"Erreur lors de la création du compte admin : {e}")