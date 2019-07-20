from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.ATTIC_APP.models import Users
import random, datetime, bcrypt

#ATTIC_APP_VIEWS
#ATTIC_APP_VIEWS
#ATTIC_APP_VIEWS

def index(request): #SECOND INDEX IE MAIN STORE PAGE
    try:
        sessionUser = request.session['user_live']
        context = {
            'thisUser': Users.objects.get(id=sessionUser),
        }
        return render(request,'ATTIC_APP/index.html', context)

    except:
        messages.error(request, 'Must be logged in first')
        return redirect('/')