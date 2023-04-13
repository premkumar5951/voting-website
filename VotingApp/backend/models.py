from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

class User(AbstractUser):
    
    username=None
    mobile = models.CharField(max_length=15, blank=True, null=True)
    adhaar = models.CharField(max_length=12, null=False, blank=False, unique=True)
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects=UserManager()
    
    USERNAME_FIELD = 'adhaar'
    REQUIRED_FIELDS=[]
        
    def __str__(self):
        return f'{self.adhaar} -> {self.get_full_name()}'
    
    def save(self, *args, **kwargs):
        try:
            self.firstname = self.first_name
            self.lastname = self.last_name
        except:
            pass
        
        super(User, self).save()
    
