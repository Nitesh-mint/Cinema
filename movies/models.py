from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="photos/movies", blank=True)
    description = models.TextField()
    length = models.CharField(max_length=100)
    trailer_link = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return self.name



