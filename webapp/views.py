from django.shortcuts import render,redirect

from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages


def home(request):
    
    return render(request,'webapp/index.html')


#register page

def register(request):
    form = CreateUserForm()

    if request.method =="POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully!")
            return redirect('login')

    context = {'form':form}

    return render(request,'webapp/register.html',context)



#user login

def loginUser(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data = request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password=password)

            if user is not None:
                auth.login(request, user)

               

                return redirect('dashboard')
    context = {'form':form}

    return render(request, 'webapp/login.html', context)


def logoutUser(request):
    auth.logout(request)

    messages.success(request,"Logged out!")
    return redirect('login')

#CRUD

#dashboard
@login_required(login_url="login")
def dashboard(request):
    records = Record.objects.all()

    context = {
       'records' : records
         }     
    return render(request, 'webapp/dashboard.html', context)

#create a reacord
@login_required(login_url="login")
def createRecord(request):
    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid:
            form.save()

            messages.success(request,"Record added!")

            return redirect('dashboard')
    
    context = {'form':form}

    return render(request,'webapp/create-record.html',context)


#update a record
@login_required(login_url="login")
def updateRecord(request, pk):
    record = Record.objects.get(id =pk)
    form = UpdateRecordForm(instance= record)

    if request.method == "POST":
        form= UpdateRecordForm(request.POST, instance =record)
        if form.is_valid:
            form.save()

            messages.success(request,"Record updated!")

            return redirect('dashboard')
        
    context = {'form':form}
    return render(request, 'webapp/update-record.html',context)


#view a record
@login_required(login_url="login")
def viewRecord(request, pk):
    all_records = Record.objects.get(id =pk)
    context = {'record':all_records}
    
    return render(request, 'webapp/view-record.html',context)

#delete a record
@login_required(login_url="login")
def deleteRecord(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()

    messages.success(request,"Record deleted!")
    return redirect('dashboard')





    