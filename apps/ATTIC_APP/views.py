from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.LOGIN_APP.models import Users
from apps.ATTIC_APP.models import Junk, Tribe, Review
import random, datetime, bcrypt


#ATTIC_APP_VIEWS
#ATTIC_APP_VIEWS
#ATTIC_APP_VIEWS

def index(request): #SECOND INDEX IE MAIN STORE PAGE
    try:
        sessionUser = request.session['user_live']
        try:
            allJunk = Junk.objects.all().order_by(request.session['sortJunk'])
        except:
            allJunk = Junk.objects.all()

        context = {
            'sessionUser': Users.objects.get(id=sessionUser),
            'allJunk': allJunk,
            'allTribes': Tribe.objects.all(),
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
        Junk.objects.create(
            name=junkName,
            description=junkDesc,
            poster=poster,
            holder=poster)    
    return redirect('/attic')

def junkPage(request, junkID): #FOR RENDERING A USERS PAGE
    context = {
        'thisJunk': Junk.objects.get(id= junkID)
    }

    return render(request, "ATTIC_APP/junkPage.html", context)

def reserveJunk(request, junkID):
    holder = Users.objects.get(id = request.session['user_live'])
    reservedjunk = Junk.objects.get(id = junkID)
    holder.holding.add(reservedjunk)
    return redirect(f'/user{holder.id}')

def deleteJunk(request, junkID):
    yourJunk = Junk.objects.get(id = junkID)
    yourJunk.delete()
    return redirect('/attic')

def reviewPoster(request, user_id):
    thisUser = Users.objects.get(id = request.session['user_live'])
    new_review = Review.objects.create(
        content = request.POST['review'],
        rating = request.POST['rate'],
        creator = thisUser
    )
    subject = Users.objects.get(id = user_id)
    subject.reviewed.add(new_review)
    return redirect(f'/user{user_id}')

def reviewJunk(request, junkID):
    thisUser = Users.objects.get(id = request.session['user_live'])
    new_review = Review.objects.create(
        content = request.POST['review'],
        rating = request.POST['rate'],
        creator = thisUser
    )
    subject = Junk.objects.get(id = junkID)
    subject.reviewed.add(new_review)
    return redirect(f'/attic/{junkID}')

def addTribe(request):
    newTribe = Tribe.objects.get(name=request.POST['addTribe']) 
    junk = Junk.objects.get(id=request.POST['thisJunk'])
    newTribe.junk.add(junk)

    return redirect('/attic')

def editJunk(request, junkID):
    print(f'this is the junk id {junkID}')
    junk_update = Junk.objects.get(id = junkID)
    junk_update.name = request.POST['name']
    junk_update.location = request.POST['location']
    junk_update.price = request.POST['price']
    junk_update.description = request.POST['description']
    junk_update.save()
    return redirect(f'/attic/{junkID}')

def sortBy(request):
    request.session['sortJunk'] = request.POST['sortJunk']
    return redirect('/attic')