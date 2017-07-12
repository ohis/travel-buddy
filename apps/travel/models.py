from __future__ import unicode_literals
from ..login_reg.models import User
from datetime import date
from datetime import datetime
from django.db import models

# Create your models here.
class TripManager(models.Manager):
    def addTrip(self,post):
        is_valid = True
        errors = []
        print date.today()
        print post.get('begin')
        print datetime.now()
        print type(date.today())
        print type(post.get('begin'))
        t = date.today()
        dt = t.strftime("%Y-%m-%d")
        print dt

        if post.get('begin') > post.get('end'):
            is_valid = False
            errors.append('Travel Date to cannot be before travel date from ')
        if len(post.get('description')) == 0:
            is_valid = False
            errors.append('description entry cannot be empty')
        if post.get('begin') < dt:
            is_valid = False
            errors.append('dates have to be future dated')
        if len(post.get('destination')) == 0:
            is_valid = False
            errors.append('destination entry cannot be empty')
        return (is_valid,errors)

        #return True
class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    other_users = models.ManyToManyField(User, related_name="other_users_trip")
    created_by = models.ForeignKey(User,related_name="trips",default=2)
    begin_date = models.DateTimeField(default=datetime.now)
    #begin_date = models.DateTimeField(default=datetime.now,blank=True)
    #begin_date = models.DateField(default=date.today)
    end_date = models.DateField(("Date"), default=date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
