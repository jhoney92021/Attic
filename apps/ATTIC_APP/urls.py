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
    url(r'^addTribe$', views.addTribe),#ADD TRIBE TO JUNK
    url(r'^review/(?P<user_id>\d+)$', views.reviewPoster),#REVIEW USER PROCESS ROUTE
    url(r'^reservejunk/(?P<junkID>\d+)$', views.reserveJunk),#RESERVE JUNK PROCESS
    url(r'^editjunk/(?P<junkID>\d+)$', views.editJunk),#DELETE JUNK PROCESS
    url(r'^deletejunk/(?P<junkID>\d+)$', views.deleteJunk),#DELETE JUNK PROCESS
    url(r'^review_junk/(?P<junkID>\d+)$', views.reviewJunk),#REVIEW JUNK PROCESS ROUTE
    url(r'^(?P<junkID>\d+)$', views.junkPage),#JUNK PAGE
    url(r'^addJunk$', views.addJunk),#ADD NEW JUNK
    url(r'^$', views.index),
]
#ATTIC_APP_URLS
#ATTIC_APP_URLS
#ATTIC_APP_URLS