from django.db import models
import re

PINCODE_REGEX = re.compile('[1-9]\d{5}$')
EMAIL_REGEX = re.compile('[a-zA-Z0-9][a-zA-Z0-9-_.]*@[a-zA-Z0-9-_]+.[a-zA-Z0-9-_]+')
MOBILE_REGEX = re.compile('[7-9]\d{9}$')

#class City()
#    city = models.CharField(max_length = 30)
#
#class State():
#    state = models.CharField(max_length = 30)
#
#class CityState():
#    city = models.ForeignKey(City)
#    state = models.ForeignKey(State)

class CityState(models.Model):
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 30)
    
    def __unicode__(self):
        return self.city + ' in '+ self.state

class Customer(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)    
    address = models.CharField(max_length = 200)
    citystate = models.ForeignKey(CityState)
    pincode = models.CharField(max_length = 10)
    mobile = models.CharField(max_length=15, unique = True)

    InvalidEmail = type('InvalidEmail', (Exception, ), {})
    InvalidPincode = type('InvalidPincode', (Exception, ), {})
    InvalidMobile = type('InvalidMobile', (Exception, ), {})

    def __unicode__(self):
        return self.name + ' with ' + self.mobile

    def save(self, *args, **kwargs):
        if not PINCODE_REGEX.match(self.pincode):
            raise self.InvalidPincode 
        if not EMAIL_REGEX.match(self.email):
            raise self.InvalidEmail 
        if not MOBILE_REGEX.match(self.mobile):
            raise self.InvalidMobile
        super(Customer, self).save(*args, **kwargs)

