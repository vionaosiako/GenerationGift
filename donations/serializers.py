from rest_framework import serializers
from .models import  Donations



class DonationsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Donations
        fields = ('items', 'name', 'location', 'time', 'donation_date', 'venue','user')