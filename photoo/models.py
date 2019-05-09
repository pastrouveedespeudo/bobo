from django.db import models


class coupe(models.Model):
        
    image = models.CharField(max_length=255)
            
    sexe = models.CharField(max_length=255)

    coiffure = models.CharField(max_length=255)
    
    haut = models.TextField()
    
    bas = models.TextField()
    
    taille_haut = models.IntegerField()
    
    taille_bas = models.IntegerField()

    



class favoris(models.Model):

    user = models.CharField(max_length=255)

    coiffure = models.CharField(max_length=255)

    hauteur = models.IntegerField()

    largeur = models.IntegerField()




























