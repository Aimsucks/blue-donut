from django.db import models
from map.models import System


class Bridge(models.Model):
    id = models.IntegerField(primary_key=True)
    from_system = models.ForeignKey(System, on_delete=models.CASCADE, related_name='+')
    to_system = models.ForeignKey(System, on_delete=models.CASCADE, related_name='+')
    owner_id = models.BigIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.from_system.name + " ≫ " + self.to_system.name)
