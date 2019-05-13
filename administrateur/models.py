from django.db import models


class image(models.Model):

    
    image = models.FileField(upload_to='bobo/')

  
