from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from . models import Donor, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@login_required(login_url='donorlogin')
def homePage(request):
    return render(request, 'index.html')


@login_required(login_url='donorlogin')
def donor(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        middlename = request.POST['middlename']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        region = request.POST['region']
        area_or = request.POST['area_or']
        town = request.POST['town']
        id_number = request.POST['id_number']
        donor_number = request.POST['donor_number']
        donor_card = request.POST['donor_card']
        name_of_patient = request.POST['patientname']
        hospital = request.POST['hospital']
        ward = request.POST['ward']
        # status = request.POST['status']

        donor = Donor(firstname=firstname, middlename=middlename, lastname=lastname,
                      email=email, phone_number=phone_number, region=region, area_or=area_or, town=town,
                      id_number=id_number, donor_number=donor_number, donor_card=donor_card,
                      name_of_patient=name_of_patient, hospital=hospital, ward=ward)
        donor.save()
        return redirect('/done')
    else:
        return render(request, 'donor.html')


def adminsignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('adminsignup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username has already been taken')
                return redirect('adminsignup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('/login')
    else:
        return render(request, 'adminsignup.html')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            print("worked")
            login(request, user)
            return redirect('/administrator')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='donorlogin')
def done(request):
    return render(request, 'done.html')

# MY CODE STARTS HERE, CREATE A VIEW FUNCTION CALLED donorlogin
# Donor Sign Up function


def donorsignup(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('donorsignup')
            else:
                user = User(first_name=first_name, last_name=last_name, email=email,
                            password=password)
                user.save()
                return redirect('/donorlogin')
    else:
        return render(request, 'donorsignup.html')

# Donor login function


def donorlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
        except:
            print("user not found")
        
        print(user)
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.info(request, "Login successfully!")
            return redirect('home')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/donor')
    else:
        return render(request, 'donorlogin.html')

# another fuction for request blood form

@login_required(login_url='donorlogin')
def requestblood(request):

    return render(request, 'requestblood.html')


def logoutView(request):
    logout(request)
    return redirect('adminsignup')


@login_required(login_url='donorlogin')
def administrator(request):
    return render(request, 'donorlogin.html')


@login_required(login_url='donorlogin')
def admins(request):
    donor = Donor.objects.all()
    return render(request, 'admins.html', {'donor': donor})

@login_required(login_url='donorlogin')
def details(request, dn):
    donor = Donor.objects.get(id=dn)
    return render(request, 'details.html', {'donor': donor})
