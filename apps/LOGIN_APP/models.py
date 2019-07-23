from __future__ import unicode_literals
from django.db import models
import re, bcrypt, datetime

#BEGIN VALIDATOR
#BEGIN VALIDATOR
#BEGIN VALIDATOR
class Manager(models.Manager):
    def validator(self, postData):
        errors = {}       

        emailFormat = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # all characters, all characters, only 3 letters
        # 8 CHARACTERS LONG, NUMBERS AND LETTERS, ONE BIG LETTER, ONE NUMBER, ONE $,!,?,@
        passwordFormat = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?=.*[\$|\?\!\@])[A-Za-z\d$!&@]{8}$')
        #GIVEN NAME FORMAT ERRORS
        if len(postData['fname']) < 2: #CHECK FOR FNAME LEN
            errors['fname'] = 'First name should be longer than 2 letters'
        if len(postData['lname']) < 2: #CHECK FOR LNAME LEN
            errors['lname'] = 'Last name should be longer than 2 letters'
        #USERNAME ERRORS
        if len(postData['username']) < 2: #CHECK FOR USERNAME LEN
            errors['username'] = 'Username should be longer than 2 characters'
        if Users.objects.filter(username=postData['username']).count() == 1: #CHECK FOR USERNAME UNIQUENESS
            errors['username'] = 'Username %s already registered' %(postData['username'])
        #BIRTHDATE ERRORS
        try:
            cutoff = datetime.datetime.now() - datetime.timedelta(days = 13 * 365) #CHECK FOR MINIMUM AGE
            date = datetime.datetime.strptime(postData["birthday"], "%Y-%m-%d")        
            if date > cutoff:
                errors["birthday"] = "Must be at least 13 years old"
        except:
            errors["birthday"] = "No date entered"
        #EMAIL ERRORS
        if not emailFormat.match(postData['email']): #CHECK FOR EMAIL FORMAT
            errors['emailmatch'] = 'Email must be formatted like, words@place.net'
        if Users.objects.filter(email=postData['email']).count() == 1: #CHECK FOR EMAIL UNIQUENESS
            errors['email'] = 'Email %s already registered' %(postData['email'])
        #PASSWORD ERRORS
        if len(postData['password']) != 8 :#CHECK FOR PASSWORD FORMAT
            errors['passlen'] = 'Passwords must be exactly 8 characters long'
        if not passwordFormat.match(postData['password']): #CHECK FOR PASSWORD FORMAT
            errors['passwordformat'] = 'Password must be formatted like, P@ssw0rd'
        if postData['password'] != postData['confirmation']: #CHECK FOR PASSWORD MATCH
            errors['password'] = 'Passwords do not match'

        return errors

#END VALIDATOR
#END VALIDATOR
#BEGIN LOGIN VALIDATOR
#BEGIN LOGIN VALIDATOR

    def loginVal(self, postData):
        errors = {}
        #EMAIL ERRORS
        if len(postData['email']) < 1 :# CHECK FOR EMAIL LENGTH
            errors['emaillen'] = 'Email field cannot be empty' 
            return errors
        if Users.objects.filter(email=postData['email']).count() == 0: #CHECK FOR EMAIL EXISTENCE
            errors['email'] = 'Email %s not a registered User' %(postData['email'])
            return errors
        #PASSWORD ERRORS
        if len(postData['password']) < 1 :#CHECK FOR LENGTH
            errors['passlen'] = 'Passwords field cannot be empty'
            return errors
        thisUser = Users.objects.get(email = postData["email"])#CHECK IF PASSWORD MATCHES USER
        if not bcrypt.checkpw(postData["password"].encode(), thisUser.password.encode()):
            errors["password"] = "Password does not match email"
        return errors

#END LOGIN VALIDATOR
#END LOGIN VALIDATOR
#BEGIN SESSION VALIDATION
#BEGIN SESSION VALIDATION

    def sessionVal(self, postData):
        errors = {'logFail' : 'Must be logged in first'}
        return errors

#END SESSION VALIDATION
#END SESSION VALIDATION
#BEGIN TABLE MODELS
#BEGIN TABLE MODELS

class Users(models.Model):
    fname = models.CharField(max_length=20, default='A person with no name apparently')
    lname = models.CharField(max_length=20, default='A person with no name apparently')
    location = models.CharField(max_length=20, default='None added yet')#LOCATION OF USER
    username = models.CharField(max_length=20, default='not a required field')
    birthday = models.DateField(default= datetime.date.today)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=80, default='Seriously, no email? it is 2019 get with it man')
    password = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()

class Company(models.Model):#A COMPANY IS USER, WHO IS LEGALLY A LLC OR HIGHER
    name = models.CharField(max_length=20)#NAME OF COMPANY
    description = models.TextField()#DESCRIPTION OF COMPANY
    administrator = models.ForeignKey(Users, related_name='company_administrator')#COMPANIES SINGLE OWNER
    employee = models.ManyToManyField(Users, related_name='company_employee', default=administrator)#OTHER USERS HOW HAVE ACCESS TO COMPANY
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()

#END TABLE MODELS
#END TABLE MODELS
