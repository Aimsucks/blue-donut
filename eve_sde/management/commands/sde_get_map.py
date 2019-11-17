from django.db import transaction

from eve_sde.models import SolarSystems, SolarSystemJumps
from eve_sde.command import SDECommand, SDE_BASE


SOLARSYSTEMS_URL = SDE_BASE + 'mapSolarSystems.csv.bz2'
STARGATES_URL = SDE_BASE + 'mapSolarSystemJumps.csv.bz2'


class Command(SDECommand):
    help = 'Downloads map data from Fuzzworks.'

    def _create_systems_helper(self, x):
        SolarSystems.objects.update_or_create(
            solarSystemID=int(x['solarSystemID']),
            solarSystemName=str(x['solarSystemName']),
            defaults=None
        )

    def _create_gates_helper(self, x):
        SolarSystemJumps.objects.update_or_create(
            fromSolarSystemID=int(x['fromSolarSystemID']),
            toSolarSystemID=str(x['toSolarSystemID']),
            defaults=None
        )

    @transaction.atomic()
    def create_systems(self):
        self._create_helper(
            SOLARSYSTEMS_URL,
            'systems',
            self._create_systems_helper,
            total=8035
        )

    @transaction.atomic()
    def create_gates(self):
        self.last_system = None
        self._create_helper(
            STARGATES_URL,
            'gates',
            self._create_gates_helper,
            total=13826)

    def handle(self, *args, **options):
        self.create_systems()
        self.create_gates()
