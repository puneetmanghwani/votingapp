from django.db import models
from django.contrib.auth.models import User

class Visited(models.Model): 
    user_name= models.CharField(primary_key=True,max_length = 200)
    # user_id= models.OneToOneField(User,on_delete=models.CASCADE)
    voted = models.BooleanField(default=False)


class Items(models.Model):
    ItemName = models.CharField(max_length = 200)
    ItemCount = models.IntegerField(blank=True, null=True)
    
    
    