from django.db import models


# Create your models here.
class Fruit(models.Model):
 fruitName = models.CharField(max_length=255)

 def __str__(self):
  return self.fruitName 