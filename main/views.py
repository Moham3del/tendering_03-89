from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as myLogin
from django.contrib.auth.decorators import login_required
from .decorators import *
from .models import *
from contract.models import Actions
# Create your views here.

from .forms import *




@login_required(login_url='login')
@allowedUsers(allowedGroups=['allowedlogin'])
def about(request):
    return render(request, 'main/about.html')


@notLoggedUser
def register(request):
    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' Created Successfully !')
            return redirect('login')

    context ={'form':form}
    return render(request, 'main/register.html', context)


@notLoggedUser
def register_ar(request):
    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' Created Successfully !')
            return redirect('login_ar')

    context ={'form':form}
    return render(request, 'main/register_ar.html', context)


@notLoggedUser
def userLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            myLogin(request, user)
            if request.user.is_staff:
                return redirect('home')
            
        else:
            messages.info(request, 'User Name or Password not Valid')

    context ={}
    return render(request, 'main/login.html', context)

@notLoggedUser
def userLogin_ar(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            myLogin(request, user)
            if request.user.is_staff:
                return redirect('home')
            
        else:
            messages.info(request, 'User Name or Password not Valid')

    context ={}
    return render(request, 'main/login_ar.html', context)


def userLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def No_Permission(request):
    context = {}
    return render(request, 'main/no_permission.html', context)

@login_required(login_url='login')
def home(request):
    user_profile = User_Profile.objects.get(user=request.user)
    user_tender_permission = User_TenderPermission.objects.get(user=request.user)
    user_contract_permission = User_ContractPermission.objects.get(user=request.user)
    user_project_permission = User_ProjectPermission.objects.get(user=request.user)
    notification = Actions.objects.all().filter(to_id=user_profile.id, is_read = False)
    notification_count = notification.count()
    context = {'user_profile':user_profile,
               'user_tender_permission':user_tender_permission,
               'user_contract_permission':user_contract_permission,
               'user_project_permission':user_project_permission,
               'notification_count':notification_count,
               }
    return render(request, 'main/home.html', context)



@login_required(login_url='login')
def user_profile(request):
    user_profile = User_Profile.objects.get(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'main/user_profile.html', context)



