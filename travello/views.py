from django.shortcuts import render,redirect
from .models import Destination
# Create your views here.
def index(request):
    dests=Destination.objects.all()

    return render(request, "index.html", {'dests': dests})


def search(request):
    bud=int(request.POST['budget'])
    
    dests=Destination.objects.filter(price__lte=bud).all()


    return render(request,'des.html',{'dests':dests})
