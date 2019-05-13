from django.db import models


class Contact(models.Model):

    nom = models.CharField(max_length=255)
    couleur_haut = models.TextField()
    couleur_bas = models.TextField()
    couleur_cheveux = models.CharField(max_length=255)
    image_vetement = models.ImageField(upload_to="static/bobo/")
    image_coupe = models.ImageField(upload_to="static/bobo/")

