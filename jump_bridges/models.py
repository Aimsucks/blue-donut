from django.db import models
from eve_sde.models import SolarSystems


class AnsiblexJumpGates(models.Model):
    structureID = models.IntegerField(primary_key=True)
    fromSolarSystemID = models.IntegerField()
    toSolarSystemID = models.IntegerField()

    def __str__(self):
        fromSolarSystem = SolarSystems.objects.values_list(
            'solarSystemName', flat=True).get(
                solarSystemID=self.fromSolarSystemID)
        toSolarSystem = SolarSystems.objects.values_list(
            'solarSystemName', flat=True).get(
                solarSystemID=self.toSolarSystemID)

        return (fromSolarSystem + " ≫ " + toSolarSystem)

# add a model for logs of who updated it to put on the route_planner page
