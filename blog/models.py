from django.db import models

# Create your models here.
class Artic(models.Model):
    artic_text = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return models.Model.__str__(self)
