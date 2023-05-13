from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Article(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(storage=S3Boto3Storage(), upload_to='articles_images/')
    promotion = models.ForeignKey('promotion.Promotion', on_delete=models.SET_NULL, null=True, blank=True)
