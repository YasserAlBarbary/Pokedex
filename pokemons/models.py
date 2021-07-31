from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    habitat = models.CharField(max_length=100)
    is_legendary = models.BooleanField(default=False)

    def __str__(self):
        return self.name
