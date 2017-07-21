from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import bcrypt
from datetime import datetime
from datetime import date

# Create your views here.
def current_user(request):
    return User.objects.get(id=request.session['user_id'])
def index(request):
    return render(request, 'travel/index.html')
def cancel_trip(request,id):
    user = User.objects.get(id=request.session['user_id'])
    trip = Trip.objects.get(id=id)
    print user.name
    others = user.other_users_trip.get(id=trip.id)

    print user.other_users_trip.remove(trip)#Cancel use this query for cancelling trip
    print trip.id
    return redirect(reverse('travel_dash'))

def remove_trip(request,id):
    user = User.objects.get(id=request.session['user_id'])
    trip = Trip.objects.get(id=id)
    print user.name
    


    print trip.id
    #Cancel use th
    #print user.trip.clear()

    print trip.delete()
    return redirect(reverse('travel_dash'))
def update_page(request):
    t = Trip.objects.get(id=request.session['trip_id'])
    context = {
       't':t
    }
    return render(request,'travel/edit.html',context)
def update(request,id):
    if request.method != 'POST':
        return redirect(reverse('update_page'))
    else:
        #user = User.objects.get(id=request.session['user_id'])
        check = Trip.objects.addTrip(request.POST)
        if check[0] == False:
            for error in check[1]:
                messages.error(request,error)
            return redirect(reverse('update_page'))
        else:
            #user = User.objects.get(id=request.session['user_id'])
            print "in update trip"
            #print user.id
            trip_update = Trip.objects.get(id=id)
            trip_update.destination = request.POST.get('destination')
            trip_update.description = request.POST.get('description')
            trip_update.begin_date = request.POST.get('begin')
            trip_update.end_date = request.POST.get('end')
            trip_update.save()
            #request.session['trip_id'] = trip.id
            #print trip.destination
            return redirect(reverse('travel_dash'))



def edit(request,id):
    t = Trip.objects.get(id=id)
    request.session['trip_id'] = t.id
    print t.id
    context = {
       't':t
    }
    return render(request,'travel/edit.html',context)
def join_trip(request,id):
    this_user = User.objects.get(id=request.session['user_id'])
    trip = Trip.objects.get(id=id)
    request.session['trip_id'] = trip.id
    print request.session['trip_id']
    print trip.id
    print "just compared trip id's"
    print this_user.id
    print "in joinTrip"
    print trip.created_by.name
    this_user.other_users_trip.add(trip)
    trip.other_users.add(this_user)
    print "new created by"
    print trip.created_by.name
    #trip.other_users.add(this_user)
    #this_user.tr
    return redirect(reverse('travel_dash'))
def show(request,id):
    user =  User.objects.get(id=request.session['user_id'])
    user_trip = Trip.objects.get(id=id)
    others_joining = user_trip.other_users.all()
    context ={
       'user':user,
       'user_trip':user_trip,
       'others_joining':others_joining
    }
    return render(request, 'travel/show.html',context)
def createTrip(request):
    return render(request,'travel/NewTrip.html')
def add_trip(request):
    if request.method != 'POST':
        return redirect(reverse('newTrip'))
    else:
        user = User.objects.get(id=request.session['user_id'])
        check = Trip.objects.addTrip(request.POST)
        if check[0] == False:
            for error in check[1]:
                messages.error(request,error)
            return redirect(reverse('newTrip'))
        else:
            user = User.objects.get(id=request.session['user_id'])
            print "in add trip"
            print user.id
            trip = Trip.objects.create(
               destination = request.POST.get('destination'),
               description = request.POST.get('description'),
               created_by = user,
               begin_date = request.POST.get('begin'),
               end_date = request.POST.get('end')
            )
            request.session['trip_id'] = trip.id
            print trip.destination
            return redirect(reverse('travel_dash'))


def disp_dash(request):
    return render(request,'travel/dashboard.html')

def dash(request):
    user = User.objects.get(id=request.session['user_id'])
    trips = Trip.objects.all().exclude(created_by=user)
    #join_trip = Trip.objects.get(id=request.session['trip_id'])
    #joined_trip = request.session['trip_id']
    #join_trip.other_users.add(user)
    #trip_added = user.other_users_trip.add(join_trip)
    all_trips_added = user.other_users_trip.all()
    #print join_trip.created_by.name
    #print join_trip.other_users.name
    #other_users_trip = trip.other_users.all()
    print date.today()
    print user.name
    context = {
       'user':user,
       'trip':user.trips.all(),
       'trips':trips,
       'other_users_trip':all_trips_added#join_trip.other_users.all()#join_trip.other_users.all()
    }
    return render(request,'travel/dashboard.html',context)

def login(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        if request.POST.get('email') == '' or request.POST.get('password') == '':
            messages.error(request, 'invalid credentials')
            return redirect('/')
        check = User.objects.loginUser(request.POST)
        if check['status'] == False:
            messages.error(request, check['message'])
            return redirect('/')
        else:
            request.session['user_id'] = check['user'].id
            return redirect('/dashboard')

def createUser(request):
	if request.method != 'POST':
		return redirect(reverse('travel_index'))
	else:
		check = User.objects.validateUser(request.POST)
		if check[0] == False:
			for error in check[1]:
				messages.error(request, error)
			return redirect(reverse('travel_index'))
		else:
			#create the user
			hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
			user = User.objects.create(
				name = request.POST.get('name'),
				email = request.POST.get('email'),
				password = hashed_pw
			)
			request.session['user_id'] = user.id
			return redirect('/dashboard')
def logout(request):
    request.session.clear()
    return redirect(reverse('travel_index'))
