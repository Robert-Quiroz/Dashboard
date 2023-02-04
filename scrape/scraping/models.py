from django.db import models

# Create your models here.
class doftDB(models.Model):
    id = models.AutoField(primary_key=True)
    pickups = models.CharField(max_length=10)
    origins = models.CharField(max_length=50)
    states_orign = models.CharField(max_length=5)
    destinations = models.CharField(max_length=50)
    states_dest = models.CharField(max_length=5)
    weights = models.CharField(max_length=10)
    distances = models.CharField(max_length=50)
    truck_types = models.CharField(max_length=5)

class routingDB(models.Model):
    id = models.AutoField(primary_key=True)