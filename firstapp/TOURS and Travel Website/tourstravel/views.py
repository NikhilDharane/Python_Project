from django.shortcuts import render
from .models import Destination

def index(request):
    dests = Destination.objects.all()
    '''
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps!!'
    dest1.price = 700
    dest1.img = 'destination_3.jpg'
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'Biryani!!'
    dest2.price = 600
    dest2.img = 'destination_5.jpg'
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Bangaluru'
    dest3.desc = 'Beautiful!!'
    dest3.price = 300
    dest3.img = 'destination_8.jpg'
    dest3.offer = False

    dests = [dest1, dest2, dest3]
    '''
    return render (request, 'index1.html', {'dests': dests})

