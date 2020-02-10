import datetime
from esipy.exceptions import APIException

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from esi import ESI


class EVEData(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True,
                                related_name='eve')

    @property
    def character_id(self):
        return self.primary_character.character_id

    @property
    def name(self):
        return self.primary_character.name

    @property
    def primary_character(self):
        return self.user.characters.all()[0]

    @property
    def all_character_ids(self):
        return self.user.characters.values_list('character_id', flat=True)


@receiver(post_save, sender=User)
def create_eve_data(sender, instance, created, **kwargs):
    if created:
        EVEData.objects.create(user=instance)


class EVEUser(models.Model):
    character_id = models.BigIntegerField(primary_key=True, db_index=True, unique=True)
    name = models.CharField(max_length=64, db_index=True, unique=True)
    owner = models.ForeignKey(User, models.CASCADE, db_index=True,
                              related_name='characters')

    alliance_id = models.BigIntegerField(default=0)
    corporation_id = models.BigIntegerField(default=0)
    esi_updated = models.DateTimeField(auto_now=True)

    scope_read_location = models.BooleanField(default=0)
    scope_write_waypoint = models.BooleanField(default=0)
    scope_search_structures = models.BooleanField(default=0)
    scope_read_structures = models.BooleanField(default=0)

    access_token = models.CharField(max_length=8192)
    refresh_token = models.CharField(max_length=8192)
    token_expiry = models.DateTimeField()

    def __str__(self):
        return self.name

    def has_perm(self, *_, **__):
        return self.is_admin

    def has_module_perms(self, _):
        return self.is_admin

    @property
    def tokens(self):
        return {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,
            'expires_in': (
                self.token_expiry - datetime.datetime.now(datetime.timezone.utc)
            ).total_seconds(),
            'token_type': 'Bearer',
        }

    @tokens.setter
    def tokens(self, token):
        self.access_token = token['access_token']
        self.refresh_token = token['refresh_token']
        self.token_expiry = (
            datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=token['expires_in']))

    def get_security(self):
        res = ESI.get_security()
        res.update_token(self.tokens)

        if res.is_token_expired(offset=60):
            try:
                self.tokens = res.refresh()
            except APIException as e:
                if e.status_code == 400:
                    self.scope_read_location = False
                    self.scope_write_waypoint = False
                    self.scope_search_structures = False
                    self.scope_read_structures = False
                    self.save()

                    raise EVEUser.KeyDeletedException(
                        "ESI refused to refresh our tokens."
                    )
                raise

        return res

    def get_client(self):
        return ESI.get_client(self.get_security())

    @property
    def is_staff(self):
        return self.is_admin

    class KeyDeletedException(Exception):
        pass
