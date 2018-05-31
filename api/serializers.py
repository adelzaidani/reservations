from rest_framework import serializers
from reservations.models import Locations, Shows


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Locations
        #fields=('id','designation','address','locality', 'website','phone')
        fields='__all__'

class ShowsSerializer(serializers.ModelSerializer):

    location=LocationSerializer()
    class Meta:
        model=Shows
        #fields=('id','title','slug','poster_url','bookable')
        fields='__all__'
