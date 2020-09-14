from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['name']
