from django.db import models


class SolarSystems(models.Model):
    solarSystemID = models.IntegerField(primary_key=True)
    solarSystemName = models.CharField(max_length=64)

    def __str__(self):
        return self.solarSystemID


class SolarSystemJumps(models.Model):
    fromSolarSystemID = models.IntegerField()
    toSolarSystemID = models.IntegerField()

    class Meta:
        unique_together = (("fromSolarSystemID", "toSolarSystemID"),)

    def __str__(self):
        return (self.fromSolarSystemID, self.toSolarSystemID)
