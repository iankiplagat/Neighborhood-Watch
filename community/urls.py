from django.urls import path, re_path
from . import views

urlpatterns=[
  path('api/neighbours/',views.NeighbourhoodList.as_view(),name='neighbor'),
  path('api/business/',views.BusinessList.as_view(),name='business'),
  path('api/users/',views.UserList.as_view(),name='users'),
]