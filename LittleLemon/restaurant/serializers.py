from rest_framework import serializers
from . models import Menu, Booking

'''
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(max_length=6)
    bookingDate = models.DateTimeField()
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    inventory = models.IntegerField(max_length=5)
    '''


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'no_of_guests', 'bookingDate']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
