from django.db import models
from django.contrib.auth.models import User

class PlannerLists(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    recents = models.CharField(max_length=8192)
    favorites = models.CharField(max_length=8192)

    def __str__(self):
        return self.user


class PopularSystems(models.Model):
    system_name = models.CharField(max_length=8192)
