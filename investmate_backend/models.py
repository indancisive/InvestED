from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=10)
    sector = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    financialReturnScore = models.DecimalField(max_digits=5, decimal_places=3)
    growthScore = models.DecimalField(max_digits=5, decimal_places=3)
    multipleScore = models.DecimalField(max_digits=5, decimal_places=3)
    integratedScore = models.DecimalField(max_digits=5, decimal_places=3)
