from django.db import models

# Create your models here.
class Promotion(models.Model):
    pourcentage = models.DecimalField(max_digits=5, decimal_places=2)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()

    def __str__(self):
        return f'{self.pourcentage}%'