import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinique.settings')

application = get_wsgi_application()

# Création et mise à jour automatique du compte Hubert
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    # Récupère le compte Hubert s'il existe, ou le crée s'il n'existe pas
    user, created = User.objects.get_or_create(
        username='Hubert',
        defaults={'email': 'hubertdanfaga383@gmail.com', 'is_staff': True, 'is_superuser': True}
    )
    
    # Applique le mot de passe H@by et les droits administrateur
    user.set_password('H@by')
    user.is_staff = True
    user.is_superuser = True
    user.save()
    
    if created:
        print("--> Compte superutilisateur 'Hubert' créé avec succès !")
    else:
        print("--> Mot de passe de 'Hubert' mis à jour avec succès !")
except Exception as e:
    print(f"Erreur lors de la création/mise à jour du compte : {e}")