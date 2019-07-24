from django.conf.urls import url
from apps.LOGIN_APP import views
# LOGIN APP IS BASE LEVEL ROUTE ('/')
# LOGIN APP IS BASE LEVEL ROUTE ('/')
# ATTIC APP IS SECONDARY LEVEL ROUTE ('/attic')
# ATTIC APP IS SECONDARY LEVEL ROUTE ('/attic')

#LOGIN_APP_URLS                    
#LOGIN_APP_URLS                    
#LOGIN_APP_URLS                    
urlpatterns = [
    url(r'^process/registrationform/company/(?P<userID>\d+)$', views.companyRegForm), #COMPANY REGISTRATION PROCESS ROUTE
    url(r'^process/registration/company/(?P<userID>\d+)$', views.processRegistrationCompany), #COMPANY REGISTRATION PROCESS ROUTE
    url(r'^process/registration$', views.processRegistration), #USER REGISTRATION PROCESS ROUTE
    url(r'^process/login$', views.processLogin), # LOGIN PROCESS ROUTE
    url(r'^company(?P<companyID>\d+)$', views.companyPage), # COMPANY PAGE
    url(r'^editaddress/(?P<userID>\d+)$', views.editAddress), # USERS PAGE
    url(r'^user(?P<userID>\d+)$', views.userPage), # USERS PAGE
    url(r'^addEmployee$', views.addEmployee), # ROUTE TO ADD EMPLOYEE
    url(r'^success/$', views.success), # SPLASH PAGE
    url(r'^logout/$', views.logout), # LOGOUT PAGE
    url(r'^$', views.index),
]
#LOGIN_APP_URLS                    
#LOGIN_APP_URLS                    
#LOGIN_APP_URLS      