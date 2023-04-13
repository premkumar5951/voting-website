from django.db import models
from backend.models import User
# Create your models here.

class ElectionParties(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='images/parties',default="images/parties/d_logo.png")
    manifesto = models.CharField(max_length=100)
    candidate_name = models.CharField(max_length=100,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.name} -> {self.candidate_name}'
    
class ElectionEvents(models.Model):
    
    is_started= models.BooleanField(default=False)
    is_ongoing= models.BooleanField(default=False)
    is_ended= models.BooleanField(default=False)
    parties= models.ManyToManyField(ElectionParties,related_name="parties")
    winner= models.ForeignKey(ElectionParties,on_delete=models.DO_NOTHING, related_name="winner" ,default="", null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='images/events',default="images/events/d_logo.png")
    description =  models.CharField(max_length=500, unique=True)
    event_date = models.DateTimeField(blank=True, null=True)
    event_end_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.name} -> {self.event_date}'
    
class PartyVotes(models.Model):
    event=models.ForeignKey(ElectionEvents,on_delete=models.DO_NOTHING)
    party=models.ForeignKey(ElectionParties,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.party.name} -> {self.event.name}'
    
class UserVotes(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    event=models.ForeignKey(ElectionEvents,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.user.adhaar} -> {self.event.name}'
    
    

