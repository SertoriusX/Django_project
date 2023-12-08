from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self) :
        return self.name
# Create your models here.
class cards_s(models.Model):
    brand = models.CharField(max_length=350)
    name = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False, null=True)


    foto = models.URLField(blank=True,null=True)
    def __str__(self) :
        return self.name
