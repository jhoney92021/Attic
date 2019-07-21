from django.conf.urls import url
from apps.ATTIC_APP import views
# LOGIN APP IS BASE LEVEL ROUTE ('/')
# LOGIN APP IS BASE LEVEL ROUTE ('/')
# ATTIC APP IS SECONDARY LEVEL ROUTE ('/attic')
# ATTIC APP IS SECONDARY LEVEL ROUTE ('/attic')

#ATTIC_APP_URLS
#ATTIC_APP_URLS
#ATTIC_APP_URLS     
urlpatterns = [
    url(r'^(?P<junkID>\d+)$', views.junkPage),#JUNK PAGE
    url(r'^addJunk$', views.addJunk),#ADD NEW JUNK
    url(r'^$', views.index),
]
#ATTIC_APP_URLS
#ATTIC_APP_URLS
#ATTIC_APP_URLS