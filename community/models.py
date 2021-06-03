from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.name
      
    def save_neighborhood(self):
      self.save()
      
    def delete_neighborhood(self):
      self.delete()  
      
    @classmethod
    def find_neighborhood(cls, name):
      return cls.objects.filter(name_icontains=name) 
    
    @classmethod
    def update_neighborhood(cls, id, name):
      update = cls.objects.filter(id=id).update(name=name)
      return update  