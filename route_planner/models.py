from django.db import models
from django.contrib.auth.models import User


class PlannerLists(models.Model):
    user = models.ForeignKey(User, models.CASCADE, db_index=True)
    recents = models.CharField(max_length=8192)
    favorites = models.CharField(max_length=8192)

    def __str__(self):
        return self.user
