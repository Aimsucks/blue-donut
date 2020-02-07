from rest_framework import serializers
from auth.models import EVEUser


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EVEUser
        fields = ['character_id', 'name', 'active']
