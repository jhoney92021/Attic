from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.LOGIN_APP.models import Users
from apps.ATTIC_APP.models import Junk, Tribe, Review, Booking
import random, datetime, bcrypt


#ATTIC_APP_VIEWS
#ATTIC_APP_VIEWS
#ATTIC_APP_VIEWS
#ATTIC_APP_VIEWS

#ATTIC MAIN PAGE
#ATTIC MAIN PAGE
#ATTIC MAIN PAGE


def index(request): #SECOND INDEX IE MAIN STORE PAGE
    try:
        sessionUser = request.session['user_live']
        try:
            allJunk = Junk.objects.all().order_by(request.session['sortJunk'])
        except:
            allJunk = Junk.objects.all()

        context = {
            'sessionUser': Users.objects.get(id=sessionUser),
            'allUsers': Users.objects.all(),
            'allJunk': allJunk,
            'allTribes': Tribe.objects.all(),
            'allBooks': Booking.objects.all(),
        }
        return render(request,'ATTIC_APP/index.html', context)

    except:
        messages.error(request, 'Must be logged in first/Failed at AtticPage')
        return redirect('/')

#ATTIC MAIN PAGE
#JUNK CRUD FUNCTIONS
#JUNK CRUD FUNCTIONS
#JUNK CRUD FUNCTIONS

def addJunk(request): #PROCESS ROUTE FOR ADDING JUNK

    poster = request.session['user_live']
    poster = Users.objects.get(id=poster)
    junkName = request.POST['name']
    junkLoc = poster.location
    junkPrice = request.POST['price']
    junkDesc = request.POST['description']
    if junkName != '':
        Junk.objects.create(
            name=junkName,
            location=junkLoc,
            price=junkPrice,
            description=junkDesc,
            poster=poster,
            holder=poster)    
    return redirect('/attic')

def sortBy(request):#SORT ROUTE
    request.session['sortJunk'] = request.POST['sortJunk']
    return redirect('/attic')

def junkPage(request, junkID): #FOR RENDERING A USERS PAGE
    thisJunk = Junk.objects.get(id= junkID)
    thisJunksBookings = Booking.objects.filter(junk=thisJunk)
    sessionUser = request.session['user_live']
    sessionUsersBooking = Booking.objects.filter(user=sessionUser)
    context = {
        'sessionUser': Users.objects.get(id=sessionUser),
        'thisJunk': thisJunk, 
        'thisJunksBookings': thisJunksBookings,       
        'sessionUsersBooking': sessionUsersBooking,       
        'allBooks': Booking.objects.all(),
    }

    return render(request, "ATTIC_APP/junkPage.html", context)

def editJunk(request, junkID):#FOR EDITING JUNK
    print(f'this is the junk id {junkID}')
    junk_update = Junk.objects.get(id = junkID)
    junk_update.name = request.POST['name']
    junk_update.location = request.POST['location']
    junk_update.price = request.POST['price']
    junk_update.description = request.POST['description']
    junk_update.save()
    return redirect(f'/attic/{junkID}')

def deleteJunk(request, junkID):
    yourJunk = Junk.objects.get(id = junkID)
    yourJunk.delete()
    return redirect('/attic')

#END JUNK CRUD FUNCTIONS
#END JUNK CRUD FUNCTIONS
#BEGIN REVIEW FUNCTIONS
#BEGIN REVIEW FUNCTIONS

def reviewPoster(request, user_id):
    liveUser = Users.objects.get(id = request.session['user_live'])
    new_review = Review.objects.create(
        content = request.POST['review'],
        rating = request.POST['rate'],
        creator = liveUser
    )
    subject = Users.objects.get(id = user_id)
    subject.reviewed.add(new_review)
    return redirect(f'/user{user_id}')

def reviewJunk(request, junkID):
    rateTotal = 0
    liveUser = Users.objects.get(id = request.session['user_live'])
    new_review = Review.objects.create(
        content = request.POST['review'],
        rating = request.POST['rate'],
        creator = liveUser
    )
    subject = Junk.objects.get(id = junkID)
    subject.reviewed.add(new_review)
    for review in subject.reviewed.all():
        rateTotal += review.rating
    rateAverage = rateTotal/subject.reviewed.all().count()
    subject.avgRating = rateAverage
    subject.save()
    print('*'*100)
    print(rateTotal)
    print(rateAverage)
    
    return redirect(f'/attic/{junkID}')

#END REVIEW FUNCTIONS
#END REVIEW FUNCTIONS
#BEGIN CATEGORY STUFF
#BEGIN CATEGORY STUFF

def addTribe(request):
    newTribe = Tribe.objects.get(name=request.POST['addTribe']) 
    junk = Junk.objects.get(id=request.POST['thisJunk'])
    newTribe.junk.add(junk)

    return redirect('/attic')

#RESERVATION STUFF
#RESERVATION STUFF

def reserveJunk(request, junkID):
    liveUser = Users.objects.get(id = request.session['user_live'])
    thisJunk = Junk.objects.get(id=junkID)
    thisJunk.reservation.add(liveUser)
    thisJunk.save()

    return redirect('/attic')

def unreserveJunk(request, junkID):
    liveUser = Users.objects.get(id = request.session['user_live'])
    thisJunk = Junk.objects.get(id=junkID)
    thisJunk.reservation.remove(liveUser)
    
    return redirect('/attic')

#RESERVATION STUFF
#RESERVATION STUFF
#HOLD STUFF
#HOLD STUFF

def holdJunk(request, junkID):#USER IN POSESSION OF ACTUALY OBJECT IS HOLDER
    liveUser = Users.objects.get(id = request.session['user_live'])
    thisJunk = Junk.objects.get(id = junkID)
    thisJunk.reservation.remove(liveUser)
    thisJunk.holder = liveUser
    thisJunk.location = liveUser.location
    thisJunk.save()
    return redirect('/attic')

def returnJunk(request, junkID):#RETURN OBJECT TO POSTER
    thisJunk = Junk.objects.get(id = junkID)
    poster = Users.objects.get(id = thisJunk.poster.id)
    thisJunk.holder = poster
    thisJunk.location = poster.location
    thisJunk.save()
    return redirect('/attic')

#HOLD STUFF
#HOLD STUFF

def bookJunk(request, junkID):#ROUTE FOR BOOKING
    sessionUser = request.session['user_live']
    sessionUser = Users.objects.get(id=sessionUser)
    thisJunk = Junk.objects.get(id=junkID)
    print('*'*50, '\n', thisJunk.booked.first, '\n','*'*50)
    newBook = Booking.objects.create(user=sessionUser, junk= thisJunk)
    return redirect('/attic/%s' %(junkID))

def unbookJunk(request, junkID):#ROUTE FOR UNBOOKING
    sessionUser = request.session['user_live']    
    sessionUser = Users.objects.get(id=sessionUser)
    thisJunk = Junk.objects.get(id=junkID)
    print('*'*50, '\n', thisJunk.booked.first, '\n','*'*50)
    UnBook = Booking.objects.get(user=sessionUser, junk= thisJunk)
    UnBook.delete()
    return redirect('/attic/%s' %(junkID))