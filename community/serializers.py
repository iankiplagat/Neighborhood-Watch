from django.db.models import fields
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    exclude = ['neighbourhood']
    
    
class NeighbourhoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Neighbourhood
    fields = ('name', 'location')    