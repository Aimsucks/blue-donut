import tempfile
import requests
import bz2
import csv
import decimal

from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.utils import IntegrityError

from map.models import Region, Constellation, System, Gate

SDE_BASE = 'https://www.fuzzwork.co.uk/dump/latest/'

REGIONS_URL = SDE_BASE + 'mapRegions.csv.bz2'
CONSTELLATIONS_URL = SDE_BASE + 'mapConstellations.csv.bz2'
SYSTEMS_URL = SDE_BASE + 'mapSolarSystems.csv.bz2'
GATES_URL = SDE_BASE + 'mapSolarSystemJumps.csv.bz2'


class Command(BaseCommand):
    help = 'Downloads SDE data from Fuzzworks.'

    def get_data_from_bz2_url(self, url):
        with tempfile.TemporaryFile() as tmp:
            tmp.write(requests.get(url).content)
            tmp.seek(0)

            with bz2.BZ2File(tmp, 'r') as uncompressed:
                data = uncompressed.read().decode()

        with tempfile.TemporaryFile(mode='w+t') as tmp:
            tmp.write(data)
            tmp.seek(0)

            for x in csv.DictReader(tmp):
                yield x

    def _create_regions_helper(self, x):
        Region.objects.update_or_create(
            id=int(x['regionID']),
            defaults={
                'name': x['regionName'],
            },
        )

    def _create_constellations_helper(self, x):
        Constellation.objects.update_or_create(
            id=int(x['constellationID']),
            defaults={
                'name': x['constellationName'],
                'region_id': int(x['regionID'])
            }
        )

    def _create_systems_helper(self, x):
        System.objects.update_or_create(
            id=int(x['solarSystemID']),
            defaults={
                'name': x['solarSystemName'],
                'region_id': int(x['regionID']),
                'constellation_id': int(x['constellationID']),
                'x': decimal.Decimal(x['x']),
                'y': decimal.Decimal(x['y']),
                'z': decimal.Decimal(x['z']),
            }
        )

    def _create_gates_helper(self, x):
        if self.last_system is None or self.last_system.id != int(x['fromSolarSystemID']):
            self.last_system = System.objects.get(id=int(x['fromSolarSystemID']))

        to_system = System.objects.get(id=int(x['toSolarSystemID']))

        from_constellation = Constellation.objects.get(id=int(x['fromConstellationID']))
        to_constellation = Constellation.objects.get(id=int(x['toConstellationID']))

        from_region = Region.objects.get(id=int(x['fromRegionID']))
        to_region = Region.objects.get(id=int(x['toRegionID']))

        try:
            Gate.objects.create(
                from_system=self.last_system,
                to_system=to_system,
                from_constellation=from_constellation,
                to_constellation=to_constellation,
                from_region=from_region,
                to_region=to_region)
        except IntegrityError:
            pass  # Don't add gates that already exist

    def _create_helper(self, url, name, fun, total=None):
        count = 0

        print(f'Starting creation of {name}...')

        for x in self.get_data_from_bz2_url(url):
            fun(x)
            count += 1

            if count % 10 == 0 or (total is not None and count == total):
                limit = 'unknown' if total is None else str(total)
                print(
                    f'    Progress: {count} out of approximately {limit}\r',
                    end=''
                )

        print(f"\nFinished creating {name} ({count} total)...")

    @transaction.atomic()
    def create_regions(self):
        self._create_helper(
            REGIONS_URL,
            'regions',
            self._create_regions_helper,
            total=106
        )

    @transaction.atomic()
    def create_constellations(self):
        self._create_helper(
            CONSTELLATIONS_URL,
            'constellations',
            self._create_constellations_helper,
            total=1146
        )

    @transaction.atomic()
    def create_systems(self):
        self._create_helper(
            SYSTEMS_URL,
            'systems',
            self._create_systems_helper,
            total=8285
        )

    @transaction.atomic()
    def create_gates(self):
        self.last_system = None
        self._create_helper(
            GATES_URL,
            'gates',
            self._create_gates_helper,
            total=13826)

    def handle(self, *args, **options):
        self.create_regions()
        self.create_constellations()
        self.create_systems()
        self.create_gates()
