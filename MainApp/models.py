from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=30)
    hex_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.TextField(default="Описание товара отсутствует")
    colors = models.ManyToManyField(to=Color)

    def __str__(self):
        return f"({self.name}) ({self.brand})"
