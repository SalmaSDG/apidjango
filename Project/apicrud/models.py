from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#Creation de la table pour enregistrer les donnees des telephone
class Dataphone(models.Model):
    RunningOn = models.TextField()
    imeiNumber=models.TextField()  # Unique IMEI
    deviceModel =models.TextField()
    apiLevel=models.TextField()
    manufactureName=models.TextField()
    deviceName=models.TextField()
    productName=models.TextField()
    cpuType=models.TextField()
    hardwareName=models.TextField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)  # Champ pour la date de création
    
    def __str__(self):
        return f"Dataphone {self.id}"
    
# Creation de la table pour enregistrer un utilisateur
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    # Ajoutez d'autres champs personnalisés si nécessaire

    def __str__(self):
        return f"UserProfile {self.id}"
