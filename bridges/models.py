from django.db import models
from map.models import System


class AnsiblexJumpGates(models.Model):
    structureID = models.IntegerField(primary_key=True)
    fromSolarSystemID = models.ForeignKey(System, on_delete=models.CASCADE)
    toSolarSystemID = models.ForeignKey(System, on_delete=models.CASCADE)
    ownerID = models.BigIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        fromSolarSystem = System.objects.get(solarSystemID=self.fromSolarSystemID)
        toSolarSystem = System.objects.get(solarSystemID=self.toSolarSystemID)
        return (fromSolarSystem + " ≫ " + toSolarSystem)
