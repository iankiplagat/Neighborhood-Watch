from django.db.models import fields
from rest_framework import serializers
from .models import *

class BusinessSerializer(serializers.ModelSerializer):
  class Meta:
    model = Business
    fields = "__all__"  
    
    
class UserSerializer(serializers.ModelSerializer):
  business=BusinessSerializer(many=True,read_only=True)
  class Meta:
    model = User
    fields = "__all__"
    
    
class NeighborhoodSerializer(serializers.ModelSerializer):
  users=UserSerializer(many=True,read_only=True)
  business=BusinessSerializer(many=True,read_only=True)
  class Meta:
    model = Neighborhood
    fields = "__all__" 
    
    
    
class ProfileSerializer(serializers.ModelSerializer):
  # user=UserSerializer(read_only=True,many=False)
  business = BusinessSerializer(many=True, read_only=True)

  class Meta:
    model = Profile
    fields="__all__"    
    
     