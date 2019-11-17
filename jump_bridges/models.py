from django.db import models


class AnsiblexJumpGates(models.Model):
    structureID = models.IntegerField(primary_key=True)
    fromSolarSystemID = models.IntegerField()
    toSolarSystemID = models.IntegerField()

    def __str__(self):
        return (self.fromSolarSystemID, self.toSolarSystemID)

# add a model for logs of who updated it to put on the route_planner page
