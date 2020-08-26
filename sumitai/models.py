from django.db import models

# Create your models here.
class SumitaiModel(models.Model):
    region = models.CharField(max_length=100)
    memo = models.TextField()
    def __str__(self):
        return self.region
