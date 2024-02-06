from django.db import models

# Create your model of Juego with name, image, description, number_players
class Juego(models.Model):
    juego_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='juego_images/') 
    description = models.TextField() 
    number_players = models.IntegerField()

     