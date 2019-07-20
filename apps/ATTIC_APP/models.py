from __future__ import unicode_literals
from django.db import models
import re, bcrypt, datetime
from apps.LOGIN_APP.models import Users
#ATTIC_APP MODELS
#ATTIC_APP MODELS
#ATTIC_APP MODELS

#BEGIN ALL TABLE MODELS
#BEGIN ALL TABLE MODELS
#BEGIN JUNK TABLE MODELS
#BEGIN JUNK TABLE MODELS
class Junk(models.Model):#ALSO REFFERED TO AS JUNK
    name = models.CharField(max_length=20)#NAME OF JUNK
    description = models.TextField()#DESCRIPTION OF JUNK
    poster = models.OneToOneField(Users, related_name='posted_junk')#PERSON WHO OWNS JUNK
    holder = models.OneToOneField(Users, related_name='rented')#PERSON IN POSSESSION  OF THE JUNK, OWNER, OR RENTER ETC 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Family(models.Model):#FOR TAGGING AN ITEM AS 'AUTOMOTIVE', OR 'KITCHEN
    name = models.CharField(max_length=20)#NAME OF FAMILY
    description = models.TextField()#DESCRIPTION OF FAMILY
    equipment = models.ManyToManyField(Junk, related_name='family')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):#EVERYTHING CAN BE REVIEWED
    content = models.TextField(max_length = 180) 
    rating = models.IntegerField()
    creator = models.ForeignKey(Users, related_name='created_review') 
    equipment = models.ManyToManyField(Junk, related_name='reviewed')
    user = models.ManyToManyField(Users, related_name='reviewed')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#END EQUIPMENT TABLE MODELS
#END EQUIPMENT TABLE MODELS


#ATTIC_APP MODELS
#ATTIC_APP MODELS
#ATTIC_APP MODELS