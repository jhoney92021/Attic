from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.LOGIN_APP.models import Users
from apps.ATTIC_APP.models import Junk, Family, Review
import random, datetime, bcrypt

#ATTIC_APP_VIEWS
#ATTIC_APP_VIEWS
#ATTIC_APP_VIEWS

def index(request): #SECOND INDEX IE MAIN STORE PAGE
    try:
        sessionUser = request.session['user_live']
        context = {
            'thisUser': Users.objects.get(id=sessionUser),
            'allJunk': Junk.objects.all(),
            'allFamilies': Family.objects.all(),
        }
        return render(request,'ATTIC_APP/index.html', context)

    except:
        messages.error(request, 'Must be logged in first/Failed at AtticPage')
        return redirect('/')

def addJunk(request): #PROCESS ROUTE FOR ADDING JUNK

    poster = request.session['user_live']
    poster = Users.objects.get(id=poster)
    junkName = request.POST['name']
    junkDesc = request.POST['description']
    if junkName != '':
        Junk.objects.create(name=junkName, description=junkDesc, poster=poster, holder=poster)    
    return redirect('/attic')