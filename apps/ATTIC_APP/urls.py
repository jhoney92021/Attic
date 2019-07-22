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
    url(r'^review/(?P<user_id>\d+)$', views.reviewPoster),
    url(r'^reservejunk/(?P<junkID>\d+)$', views.reserveJunk),
    url(r'^deletejunk/(?P<junkID>\d+)$', views.deleteJunk),
    url(r'^review_junk/(?P<junkID>\d+)$', views.reviewJunk),#JUNK PAGE
    url(r'^(?P<junkID>\d+)$', views.junkPage),#JUNK PAGE
    url(r'^addJunk$', views.addJunk),#ADD NEW JUNK
    url(r'^$', views.index),
]
#ATTIC_APP_URLS
#ATTIC_APP_URLS
#ATTIC_APP_URLS