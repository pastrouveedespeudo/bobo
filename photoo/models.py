from django.db import models


class categorie(models.Model):
    
    name_categorie = models.CharField(max_length=60)
    


class aliment(models.Model):
    name_aliment = models.CharField(max_length=60)
    code_product_food = models.CharField(max_length=20)
    description = models.TextField()
    nutriscore = models.CharField(max_length=1)
    image = models.ImageField()
    name_store = models.CharField(max_length=60)
    name_brand = models.CharField(max_length=60)

    id_categorie = models.ForeignKey(categorie, on_delete=models.CASCADE)




class recherche(models.Model):
    
    recherche = models.CharField(max_length=255)
            



class substitut(models.Model):
    
    name_aliment = models.CharField(max_length=60)
    code_product_food = models.CharField(max_length=20)
    description = models.TextField()
    nutriscore = models.CharField(max_length=1)
    image = models.ImageField()
    name_store = models.CharField(max_length=60)
    name_brand = models.CharField(max_length=60)









    
