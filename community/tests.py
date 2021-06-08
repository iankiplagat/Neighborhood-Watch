from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

# Create your tests here.
class NeighborHoodTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.neighborhood = Neighborhood(name = 'name', location = 'location', 
                                         neighborhood_desc = 'neighborhood_desc',
                                         occupants_count = 0, health_tell = 0,
                                         police_number = 0)
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood,Neighborhood))
        
    # Testing Save Method
    def test_save_method(self):  
        self.neighborhood.save_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) > 0)
        
    def tearDown(self):
        Neighborhood.objects.all().delete()
     
    # Testing Delete Method  
    def delete_neighborhood(self):
        self.delete() 
        
    # Testing Update Method    
    def test_update_neighborhood(self):
        self.neighborhood.save_neighborhood()
        self.neighborhood.update_neighborhood(self.neighborhood.id,'name')
        update=Neighborhood.objects.get(name = 'name', location = 'location', 
                                        neighborhood_desc = 'neighborhood_desc',
                                         occupants_count = 0, health_tell = 0,
                                         police_number = 0)
        self.assertEqual(update.name,'name')  
        
        
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User()
        self.neighborhood = Neighborhood()
        self.user.save()
        self.neighborhood.save()
        self.profile = Profile(user = self.user, name = 'name', 
                               profile_pic = 'img', email = 'test@gmail.com', 
                               neighborhood = self.neighborhood)
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
    # Testing Save Method
    def test_save_method(self):  
        self.profile.save_user_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        
    def tearDown(self):
        Profile.objects.all().delete()
     
    # Testing Delete Method  
    def delete_profile(self):
        self.delete() 
        
    # Testing Update Method    
    @classmethod
    def test_update_profile(self):
        self.profile.save_user_profile()
        self.profile.update_profile(self.profile.id,'name')
        update=Profile.objects.get(user = self.user, name = 'name', 
                                   profile_pic = 'img', email = 'test@gmail.com', 
                                   neighborhood = self.neighborhood)
        self.assertEqual(update.name,'name')                        
        
