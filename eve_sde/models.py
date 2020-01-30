from django.db import models


class SolarSystems(models.Model):
    solarSystemID = models.IntegerField(primary_key=True)
    solarSystemName = models.CharField(max_length=64)
    x = models.FloatField(default=None)
    y = models.FloatField(default=None)
    z = models.FloatField(default=None)

    def __str__(self):
        return self.solarSystemID


class SolarSystemJumps(models.Model):
    fromSolarSystemID = models.IntegerField()
    toSolarSystemID = models.IntegerField()
    fromConstellationID = models.IntegerField(default=None)
    toConstellationID = models.IntegerField(default=None)
    fromRegionID = models.IntegerField(default=None)
    toRegionID = models.IntegerField(default=None)

    class Meta:
        unique_together = (("fromSolarSystemID", "toSolarSystemID"),)

    def __str__(self):
        return (self.fromSolarSystemID, self.toSolarSystemID)
