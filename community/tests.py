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
        self.user.save()
        self.neighborhood = Neighborhood()
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
        
        
class BusinessTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.profile = Profile()
        self.profile.save()
        self.neighborhood = Neighborhood()
        self.neighborhood.save()
        self.business = Business(name = 'name', business_desc = 'desc', 
                                         profile = self.profile,
                                         business_email = 'email',
                                         neighborhood = self.neighborhood)
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
        
    # Testing Save Method
    def test_save_method(self): 
        self.business.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)
        
    def tearDown(self):
        Business.objects.all().delete()
        Profile.objects.all().delete()
        Neighborhood.objects.all().delete()
     
    # Testing Delete Method  
    def delete_business(self):
        self.delete() 
        
    # Testing Update Method    
    def test_update_business(self):
        self.business.save_business()
        self.business.update_business(self.business.id,'name')
        update=Business.objects.get(name = 'name', business_desc = 'desc', 
                                         profile = self.profile,
                                         business_email = 'email',
                                         neighborhood = self.neighborhood)
        self.assertEqual(update.name,'name')                           
        

