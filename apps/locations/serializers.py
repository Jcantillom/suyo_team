from rest_framework import serializers
from .models import LocationModel


class LocationSerializer(serializers.ModelSerializer):
    class Meta():
        model = LocationModel
        fields = "__all__"
