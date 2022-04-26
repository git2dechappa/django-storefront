from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x=1
    y=2
    return x


# Create your views here.
def say_hello(request):
    x=calculate()
    y=2
#    return HttpResponse("Hello World")
    return render(request, "hello.html",{"name": "Oli"})

def show_fees(request):
    x=calculate()
    y=2
#    return HttpResponse("Hello World")
    return render(request, "Test Page 2.html",{"name": "Oli"})

def show_fees2(request):
    x=calculate()
    y=2
#    return HttpResponse("Hello World")
    return render(request, "DW.html",{"name": "Oli"})