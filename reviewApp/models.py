from django.db import models


# Create your models here.
class Cocktails (models.Model):
    name = models.CharField(max_length=200, default="")
    alcoholPercent = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
    glass = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name
