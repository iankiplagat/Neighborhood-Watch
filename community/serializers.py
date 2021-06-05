from rest_framework import serializers
from .models import *
from django import forms

class BusinessSerializer(serializers.ModelSerializer):
  class Meta:
    model = Business
    fields = "__all__"  
    
    
class UserSerializer(serializers.ModelSerializer):
  email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
  class Meta:
    model = User
    fields = ['username','email','password']
    
    
class NeighborhoodSerializer(serializers.ModelSerializer):
  users=UserSerializer(many=True,read_only=True)
  business=BusinessSerializer(many=True,read_only=True)
  class Meta:
    model = Neighborhood
    fields = "__all__" 
    
    
class ProfileSerializer(serializers.ModelSerializer):
  business = BusinessSerializer(many=True, read_only=True)

  class Meta:
    model = Profile
    fields="__all__"    
    
       
class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = "__all__"    
    
     