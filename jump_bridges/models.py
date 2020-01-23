from django.db import models
from eve_sde.models import SolarSystems


class AnsiblexJumpGates(models.Model):
    structureID = models.IntegerField(primary_key=True)
    fromSolarSystemID = models.IntegerField()
    toSolarSystemID = models.IntegerField()

    ownerID = models.BigIntegerField()

    def __str__(self):
        fromSolarSystem = SolarSystems.objects.values_list(
            'solarSystemName', flat=True).get(
                solarSystemID=self.fromSolarSystemID)
        toSolarSystem = SolarSystems.objects.values_list(
            'solarSystemName', flat=True).get(
                solarSystemID=self.toSolarSystemID)

        return (fromSolarSystem + " ≫ " + toSolarSystem)


"""
Add a model for alliances that is *easily* editable from the admin interface (including order!)
    for searching with the new jump gate automation tool.

List:
1. TEST
2. BRAVE
3. REQ
4. IOU
5. VINDI
6. W4RP
7. AOM
"""
