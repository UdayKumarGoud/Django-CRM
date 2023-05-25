from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages

def home(request):
    #check to see if logged in
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        #authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            messages.success(request,'You have successfully loged in')
            return redirect('home')
        else:
            messages.success(request,'there was an error in logging please try again')
            return redirect('home')
    else:   
        return render(request,'home.html',{})


def logout_user(request):
    messages.success(request,"you have successfully logout")
    return redirect ('home')