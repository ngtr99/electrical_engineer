from django.db import models

class ElectricalData(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    picture_url = models.URLField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name