from rest_framework import serializers
from .models import Names

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Names
        