from django.shortcuts import render, redirect, get_object_or_404
from .models import Staffs_profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Staffsform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exit")


        user = authenticate(request, username=username, password = password)

        if user is not None:
                login(request, user)
                return redirect('Home')
            
    context = {}
    return render(request, 'login_page.html', context)

def logout_user(request):
    logout(request)
    return redirect('Home')



def staffs_list(request):
    staffs = Staffs_profile.objects.all()

    return render(request, 'staffs.html', {'staffs':staffs})

@login_required(login_url='login')
def create_profile(request):
    staffs = Staffs_profile.objects.all()
    form = Staffsform()
    Levels = Staffs_profile.objects.all()

    if request.method == 'POST':
        form = Staffsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    return render(request, 'create_staff_profile.html', {'staffs':staffs, 'form':form})

@login_required(login_url='login')
def update_profile(request, pk):
    staffs = Staffs_profile.objects.get(id=pk)
    updateform = Staffsform(instance = staffs)
    if request.method == 'POST':
        updateform = Staffsform(request.POST, instance = staffs)

        if updateform.is_valid():
            updateform.save()
            return redirect('Home')

    return render(request, 'update_profile_page.html', {'staffs':staffs, 'updateform':updateform} )

@login_required(login_url='login')
def delete_profile(request, pk):
    staffs = Staffs_profile.objects.get(id = pk)
    if request.method == 'POST':
        staffs.delete()
        return redirect('Home')
    return render(request, 'delete_profile.html' )

@login_required(login_url='login')
def Staffprofile(request,pk):
   staff = Staffs_profile.objects.get(id=pk)
   return render(request, 'profile_page.html', {'staff':staff})