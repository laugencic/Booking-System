from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
def home(request):
    return render(request,'core/main.html')

def register_user(request):
    if request.method=="POST":
        username=request.POST.get(username)
        First_name=request.POST.get(First_name)
        Last_name=request.POST.get(Last_name)
        email=request.POSt.get(email)
        password=request.POST.get(password)

    return render(request,'core/register.html')

def login(request):
    # if request.method=="GET":
    #     username=request.GET.get(username)        
    #     password=request.GET.get(password)
    return render(request,'core/login.html')

def profile(request):
    return render(request,'core/profile.html')

def bus_ticket(request):
    return render(request,'core/bus.html')

def book_hotel(request):
    return render(request,'core/hotel.html')

def logout(request):
    return render(request,'core/logout.html' )