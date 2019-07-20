from django.conf.urls import url
from apps.ATTIC_APP import views

#ATTIC_APP_URLS
#ATTIC_APP_URLS
#ATTIC_APP_URLS     
urlpatterns = [
    url(r'^$', views.index),
    url(r'^addJunk$', views.addJunk),#ADD NEW JUNK
]
#ATTIC_APP_URLS
#ATTIC_APP_URLS
#ATTIC_APP_URLS