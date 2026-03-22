from django.db import models

# Create your models here.
class ElectricalData(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    picture = models.URLField(blank=True, null=True)
    skills = models.TextField(blank = True, null = True)
    def __str__(self):
        return self.name