from django.db import models


class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, db_index=True)

    def __str__(self):
        return self.name


class Constellation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, db_index=True)

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        db_index=True
    )

    def __str__(self):
        return self.name


class System(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, db_index=True)

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        db_index=True
    )

    constellation = models.ForeignKey(
        Constellation,
        on_delete=models.CASCADE,
        db_index=True
    )

    x = models.DecimalField(max_digits=35, decimal_places=10)
    y = models.DecimalField(max_digits=35, decimal_places=10)
    z = models.DecimalField(max_digits=35, decimal_places=10)

    gates = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Gate',
        through_fields=('from_system', 'to_system'),
        related_name='gate_set',
    )

    """
    Consider adding:

    bridges = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Bridges',
        through_fields=('from_system', 'to_system'),
        related_name='bridge_set',
    )

    This would mean that we need a table for bridges, which I want to do separately.
    """

    def __str__(self):
        return self.name


class Gate(models.Model):
    class Meta:
        unique_together = ('from_system', 'to_system')

    from_system = models.ForeignKey(System, models.DO_NOTHING, related_name='+')
    to_system = models.ForeignKey(System, models.DO_NOTHING, related_name='+')

    from_constellation = models.ForeignKey(Constellation, models.DO_NOTHING, related_name='+')
    to_constellation = models.ForeignKey(Constellation, models.DO_NOTHING, related_name='+')

    from_region = models.ForeignKey(Region, models.DO_NOTHING, related_name='+')
    to_region = models.ForeignKey(Region, models.DO_NOTHING, related_name='+')
