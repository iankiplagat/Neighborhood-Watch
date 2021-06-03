from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from django.http import response
from .models import *
from .serializers import *

# Create your views here.
class NeighborhoodList(APIView):
  def get_neighborhood(self, pk):
    try:
        return Neighborhood.objects.get(pk=pk)
    except Neighborhood.DoesNotExist:
        return Http404()

  def get(self,request,format=None):
    neighborhood= Neighborhood.objects.all()
    serializers=NeighborhoodSerializer(neighborhood, many=True)
    return Response(serializers.data)

  def post(self,request,format=None):
    serializers=NeighborhoodSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_200_OK)
    return Response(serializers.errors , status= status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None):
    neighborhood = self.get_neighborhood(pk)
    serializers = NeighborhoodSerializer(neighborhood, request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    neighborhood = self.get_neighborhood(pk)
    neighborhood.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class BusinessList(APIView):
  def get_business(self, pk):
    try:
        return Business.objects.get(pk=pk)
    except Business.DoesNotExist:
        return Http404()

  def get(self, request,format=None):
    business=Business.objects.all()
    serializers=BusinessSerializer(business, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers=BusinessSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None):
    business = self.get_business(pk)
    serializers = BusinessSerializer(business, request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    business = self.get_business(pk)
    business.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):
  def get_users(self,pk):
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404()

  def get(self,request,pk,format=None):
    users=self.get_users(pk)
    serializers=UserSerializer(users, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers=UserSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()

      users=serializers.data
      response={
        'data':{
          'users':dict(users),
          'status':'success',
          'message':'user created successfully',
        }

      }

      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self,request,pk,format=None):
    users=User.objects.get(pk-pk)
    serializers=UserSerializer(users,request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
  def delete(self,request,pk,format=None):
    users=self.get_users(pk)
    users.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)