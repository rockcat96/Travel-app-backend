from .models import Countries
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our CountriesySerializer
class CountriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Countries
        fields = ['id', 'name', 'cities', 'month', 'days', 'url']
        