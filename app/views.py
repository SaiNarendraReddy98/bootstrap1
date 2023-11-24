from django.shortcuts import render

# Create your views here.
def webpage(request):
    return render(request,'webpage.html')

def login(request):
    return render(request,'login.html')

def andhra(request):
    return render (request,'andhra.html')

def bangalore(request):
    return render (request,'bangalore.html')

def jandk(request):
    return render (request,'jandk.html')

def vizag(request):
    return render (request,'vizag.html')

def hyd(request):
    return render (request,'hyd.html')

def coim(request):
    return render(request,'coim.html')