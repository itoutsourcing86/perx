from django.db import models


# Create your models here.


class Key(models.Model):

    STATUS = (
        ('0', 'Not Issued'),
        ('1', 'Issued'),
        ('2', 'Used'),
    )

    key = models.CharField(max_length=4, unique=True)
    status = models.CharField(max_length=1, choices=STATUS, default='0')

    def __str__(self):
        return self.key

    class Meta:
        ordering = ['-status']
