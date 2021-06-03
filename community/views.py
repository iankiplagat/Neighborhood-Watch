from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
# Create your views here.
class NeighborhoodList(APIView):
  def get(self, request, format=None):
    neighborhood = Neighborhood.objects.all()
    serializers = NeighborhoodSerializer(neighborhood, many=True)
    return Response(serializers.data)
  
  def post(self, request, format=None):
        serializers = NeighborhoodSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
class BusinessList(APIView):
  def get(self, request, format=None):
    business = Business.objects.all()
    serializers = BusinessSerializer(business, many=True)
    return Response(serializers.data) 
  
  def post(self, request, format=None):
        serializers = BusinessSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)       
      
      
class UserList(APIView):
  def get(self, request, format=None):
    users = User.objects.all()
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data)  
  
  def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
      