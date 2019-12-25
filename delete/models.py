from django.db import models


class Subscriber(models.Model):
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    ha1 = models.CharField(max_length=128)
    ha1b = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'subscriber'
        unique_together = (('username', 'domain'),)

    def __str__(self):
        return self.username

# Create your models here.
