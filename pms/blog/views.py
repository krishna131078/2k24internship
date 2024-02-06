from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("hello world")


def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    name="royal"
    age=20

    context={
        "name":name,
        "age":age

    }

    return render(request,"blog/contactus.html",context)
