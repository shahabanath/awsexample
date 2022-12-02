from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import datetime

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **other_fields):
        """
        Create and save a user with the given email and password. And any other fields, if specified.
        """
        if not email:
            raise ValueError('An Email address must be set')
        email = self.normalize_email(email)
        
        user = self.model(email=email, **other_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def _create_user_phone(self, phonenumber, password,otp, **other_fields):
        """
        Create and save a user with the given email and password. And any other fields, if specified.
        """
        if not phonenumber:
            raise ValueError('Phone number is mandatory')
        
        user = self.model(phonenumber=phonenumber,password=password,otp=otp, **other_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_user_phone(self, phonenumber, password,otp, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user_phone(phonenumber, password,otp,**other_fields)

    def create_user(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **other_fields)

class User(AbstractUser):
    username=models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=50, null=True,blank=True,unique=True)
    phonenumber = models.IntegerField(unique=True)
    SELECT_ROLE = (('admin', 'admin'),('mechanic', 'mechanic'),('user','user'))
    role=models.CharField(max_length=11,choices=SELECT_ROLE)
    dob=models.DateField(null=True)
    otp=models.IntegerField(null=True,default=None)
    TYPE_SELECT = (('male', 'Male'),('female', 'Female'),('others','others'))
    gender=models.CharField(max_length=11,choices=TYPE_SELECT)
    image = models.ImageField(upload_to='profilefotos/',null=True,blank=True)
    place = models.CharField(max_length=100,null=True,blank=True)
    APPROVED_CHOICES = (('approved','approved'),('disapproved','disapproved'))
    is_approved= models.CharField(choices=APPROVED_CHOICES,default='disapproved',max_length=15)
    RENEW_CHOICES = (('renew','renew'),('notrenew','notrenew'))
    renew= models.CharField(choices=RENEW_CHOICES,default='notrenew',max_length=15)
    workshop_name=models.CharField(max_length=100,null=True,blank=True)
    longitude=models.FloatField(null=True)
    latitude=models.FloatField(null=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    rating = models.IntegerField(default=0)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phonenumber']
    objects = UserManager()

    # def get_username(self):
    #     return self.email
    def __str__(self):
        return str(self.username)

class insurance(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle_no=models.CharField(max_length=100,null=True,blank=True)
    cc=models.IntegerField()
    VEH_TYPE = (('car','car'),('bike','bike'),('commercial vehicles','commercial vehicles'))
    vehicle_type= models.CharField(choices=VEH_TYPE,null=True,max_length=50)
    FUEL_TYPE = (('petrol','petrol'),('diesel','diesel'),('others','others'))
    fuel= models.CharField(choices=FUEL_TYPE,null=True,max_length=50)
    vehicle_model= models.CharField(max_length=100,null=True,blank=True)
    place= models.CharField(max_length=100,null=True,blank=True)
    brand= models.CharField(max_length=100,null=True,blank=True)
    coverage= models.CharField(max_length=100,null=True,blank=True)
    issue_date=models.DateTimeField()
    expiry_date=models.DateTimeField()
    INSURANCE_STATUS = (('requested','requested'),('renewed','renewed'))
    status= models.CharField(choices=INSURANCE_STATUS,default='requested',max_length=15)
    image = models.ImageField(upload_to='vehiclefotos/',null=True,blank=True)
    
    
