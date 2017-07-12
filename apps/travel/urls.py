from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$',views.index ,name ='travel_index'),
    url(r'^dashboard$',views.dash ,name ='travel_dash'),
    url(r'^display$',views.disp_dash ,name ='disp_dash'),
    url(r'^update$',views.update_page ,name ='update_page'),
    url(r'^create$',views.createUser ,name ='create'),
    url(r'^destroy$',views.logout ,name ='destroy'),
    url(r'^login$',views.login ,name ='login'),
    url(r'^createTrip$',views.createTrip ,name ='newTrip'),
    url(r'^addTrip$',views.add_trip ,name ='add_trip'),
    url(r'^show/(?P<id>\d+)$',views.show ,name ='show'),
    url(r'^edit/(?P<id>\d+)$',views.edit ,name ='edit'),
    url(r'^join_trip/(?P<id>\d+)$',views.join_trip ,name ='joinTrip'),
    url(r'^remove/(?P<id>\d+)$',views.remove_trip ,name ='remove'),
    url(r'^update_trip/(?P<id>\d+)$',views.update ,name ='update'),
    #url(r'^',include('apps.formtest.urls')),
]
