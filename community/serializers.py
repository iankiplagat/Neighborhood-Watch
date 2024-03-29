from rest_framework import serializers
from .models import *
from django import forms

class BusinessSerializer(serializers.ModelSerializer):
  class Meta:
    model = Business
    fields = "__all__"  
    
    
class UserSerializer(serializers.ModelSerializer):
  email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
  
  password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
  class Meta:
    model = User
    fields = ['username','email','password', 'password2']
    extra_kwargs = {
      "password": {'write_only': True}
    }
    
  def save(self):
    user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
        )
    password = self.validated_data['password']
    password2 = self.validated_data['password2']
      
      
    if password != password2:
      raise serializers.ValidationError({'password': 'Passwords must match'}) 
    
    user.set_password(password)
    user.save()
    return user
  
  

class LoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField(
        min_length=8,
        max_length=20,
        write_only=True,
        error_messages={
            "min_length": "Password should be atleast {min_length} characters"
        }

    )
    class Meta:
        model=User
        fields=["username", "password"]  
    
    
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
    
     