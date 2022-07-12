from rest_framework import serializers
from .models import  Donations



class DonationsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Donations
        fields = ('id','poster', 'items', 'donorname', 'location', 'time', 'donationdate','user')
        