from rest_framework import serializers
from planner.models import PlannerLists


class ListSerializer(serializers.Serializer):
    systems = StringListField()

class StringListField(serializers.ListField):
    child = serializers.CharField()
