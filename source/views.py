from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    return  render(request,'home.html',{'name':'vikas'})



def add(request):
    a=int(request.POST['num1'])
    b=int(request.POST['num2'])
    c=a+b
    return render(request,'res.html',{'result':c})