from django.db import models



# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)  # Adjust the max_length as needed
    author = models.CharField(max_length=100)  # Adjust the max_length as needed
    genre = models.CharField(max_length=100)  # Adjust the max_length as needed
    publicationyear = models.CharField(max_length=4)
      # Assuming it's a year, so set max_length as needed
    isbn=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.title




