from django.db import models

class DefaultLink(models.Model):
    original_link = models.CharField()
    shortlink = models.CharField(max_length=50)

    def __str__(self):
        return f"Original: {self.original_link} | Short: {self.shortlink}"