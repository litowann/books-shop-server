from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    pages = models.IntegerField()
    author = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.name