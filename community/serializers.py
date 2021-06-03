from django.db.models import fields
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    exclude = ['neighbourhood']
    
    
class NeighborhoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Neighborhood
    fields = ('name', 'location')  
    
    
class BusinessSerializer(serializers.ModelSerializer):
  class Meta:
    model = Business
    fields = ('name', 'email')      