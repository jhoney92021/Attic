from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.LOGIN_APP.models import Users, Company
import random, datetime, bcrypt

#LOGIN_APP_VIEWS
#LOGIN_APP_VIEWS
#LOGIN_APP_VIEWS

#BEGIN_LOGIN_PAGE_ROUTES
#BEGIN_LOGIN_PAGE_ROUTES
#BEGIN_LOGIN_PAGE_ROUTES
def index(request): #MAIN INDEX IE LOGIN INDEX
    return render(request,'LOGIN_APP/index.html')

def processRegistration(request): #REGISTRATION PROCESS ROUTE
    errors = Users.objects.validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')
    else:
        newUserPass = request.POST['password']
        newUserPassEncrypt = bcrypt.hashpw(newUserPass.encode(), bcrypt.gensalt())

        newUser = Users.objects.create(
        fname= request.POST['fname'],
        lname= request.POST['lname'],
        username= request.POST['username'],
        birthday= request.POST['birthday'],
        email= request.POST['email'],
        password= newUserPassEncrypt
           )
        request.session['user_live'] = newUser.id
        return redirect('/attic')

def processLogin(request): #LOGIN PROCESS ROUTE    
    errors = Users.objects.loginVal(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')

    userQuery = Users.objects.get(email= request.POST['email'])
    request.session['user_live'] = userQuery.id
    return redirect('/attic' )

#END_LOGIN_PAGE_ROUTES
#END_LOGIN_PAGE_ROUTES
#BEGIN_SUCCESS_PAGE_ROUTES
#BEGIN_SUCCESS_PAGE_ROUTES

def success(request): #RENDER SUCCESS, TO INFORM THE USER THAT THEY ARE IN SESSION
    try:
        liveUser = request.session['user_live']
        context ={
        'user': Users.objects.get(id = liveUser),
        }
        return render(request, 'LOGIN_APP/success.html', context)
    except:
        messages.error(request, 'Must be logged in first')
        return redirect('/')

def logout(request): #CLEAR USER IN SESSION
    request.session.clear()
    return redirect('/')

#END_SUCCESS_PAGE_ROUTES
#END_SUCCESS_PAGE_ROUTES
#BEGIN USER RELATED FUNCTIONS
#BEGIN USER RELATED FUNCTIONS
#BEGIN USER RELATED FUNCTIONS

def userPage(request, userID): #FOR RENDERING A USERS PAGE
    sessionUser = request.session['user_live']
    context = {
        'thisUser': Users.objects.get(id= userID),
        'sessionUser': Users.objects.get(id=sessionUser),

    }

    return render(request, "LOGIN_APP/userPage.html", context)


#COMPANY STUFF
#COMPANY STUFF
#COMPANY STUFF
#COMPANY STUFF

def companyPage(request, companyID): #FOR RENDERING A COMPANY PAGE
    try:
        liveUser = request.session['user_live']
        context = {
            'thisCompany': Company.objects.get(id= companyID),
            'liveUser': Users.objects.get(id=liveUser),
        }

        return render(request, "LOGIN_APP/companyPage.html", context)
    except:
        messages.error(request, 'Must be logged in first/BROKE AT COMPANY PAGE')
        return redirect('/')

def addEmployee(request):#ADDING EMPLOYEES
    newEmployee = request.POST['empname']
    newEmployee = Users.objects.get(username=newEmployee)
    thisCompany = request.POST['thisCompany']
    thisCompany = Company.objects.get(id=thisCompany)
    thisCompany.employee.add(newEmployee)
    thisCompany.save()
    return redirect('/company%s' %(thisCompany.id))
    

def companyRegForm(request, userID):#COMPANY REGISTRATION FORM
    context = {
        'thisUser': Users.objects.get(id= userID),

    }

    return render(request, "LOGIN_APP/companyForm.html", context)


def processRegistrationCompany(request, userID): #COMPANY REGISTRATION PROCESS ROUTE
    errors = Company.objects.sessionVal(request.POST)
    if len(errors) > 1:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')
    else:

        newCompany = Company.objects.create(
        name= request.POST['name'],
        description= request.POST['description'],
        administrator= Users.objects.get(id=userID),
           )
        return redirect('/user%s' %(userID))

#LOGIN_APP_VIEWS
#LOGIN_APP_VIEWS
#LOGIN_APP_VIEWS
#LOGIN_APP_VIEWS