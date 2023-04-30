from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# User = get_user_model()
# Donor =get_user_model()

# Create your models here.
status_choice = (('approved', 'APPROVED'), ('pending', 'PENDING'), ('rejected', 'REJECTED'))

region_choice = (('ahafo', 'Ahafo Region'), ('ashanti', 'Ashanti Region'), ('bono', 'Bono East Region'),
                 ('brong', 'Brong Ahafo Region'), ('central', 'Central Region'), ('eastern', 'Eastern Region'),
                 ('greater', 'Greater Accra Region'), ('north east', 'North East Region'), ('northern', 'Northern Region'),
                 ('oti', 'Oti Region'), ('savannah', 'Savannah Region'), ('upper east', 'Upper East Region'),
                 ('upper west', 'Upper West Region'), ('western', 'Western Region'), ('western north', 'Western North Region'),
                 ('volta', 'Volta Region'))

# user models
class User(AbstractUser):
    username=models.CharField(max_length=20, default='')
    fist_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.first_name



# Blood donor Models
class Donor(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    firstname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30, default='')
    lastname = models.CharField(max_length=30, default='')
    email = models.CharField(default='', max_length=50)
    phone_number = models.CharField(max_length=10, default='##########')
    region = models.CharField(max_length=30, choices= region_choice, default='ahafo')
    area_or = models.CharField(max_length=30, default='Area')
    town = models.CharField(max_length=30, default='')
    id_number = models.CharField(default='GHA-###########-1', max_length=30)
    donor_number = models.IntegerField(default=0)
    donor_card = models.CharField(default='NBS/20/##########/', max_length=30)
    name_of_patient = models.CharField(max_length=200, default='')
    hospital = models.CharField(max_length=200, default='')
    ward = models.CharField(max_length=10, default='Ward #')
    # status = models.CharField(max_length=10, choices = status_choice, default='pending')
    
    def __str__(self):
        return self.firstname

