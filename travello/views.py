from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_4.jpg'
    dest1.price = 700
    dest1.offer=False

    dest2 = Destination()
    dest2.name = 'Kashmir'
    dest2.desc = "Beauty of kashmir can't compared with others"
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    dest2.offer=True

    dest3 = Destination()
    dest3.name = 'Maldives'
    dest3.desc = 'Sunny side of life'
    dest3.img = 'destination_1.jpg'
    dest3.price = 750
    dest3.offer=False



    dest4=Destination()
    dest4.name='Vizag'
    dest4.price=1000
    dest4.img='destination_9.jpg'
    dest4.desc='you should visit beach '
    dest4.offer=False


    dest5=Destination()
    dest5.name='Goa'
    dest5.price=500
    dest5.img='destination_3.jpg'
    dest5.desc='cold breeze adventure in your soul goa is calling'
    dest5.offer=True


    dest6=Destination()
    dest6.name='Manali'
    dest6.price=600
    dest6.img='destination_7.jpg'
    dest6.desc='ready for unlimited adventure opportunities'
    dest6.offer=True

    dests = [dest1, dest2, dest3,dest4,dest5,dest6]

    return render(request, "index.html", {'dests': dests})
