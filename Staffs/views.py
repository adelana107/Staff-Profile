from django.shortcuts import render, redirect, get_object_or_404
from .models import Staffs_profile
from .forms import Staffsform


# Create your views here.



def staffs_list(request):
    staffs = Staffs_profile.objects.all()

    return render(request, 'staffs.html', {'staffs':staffs})


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


def update_profile(request, pk):
    staffs = Staffs_profile.objects.get(id=pk)
    updateform = Staffsform(instance = staffs)
    if request.method == 'POST':
        updateform = Staffsform(request.POST, instance = staffs)

        if updateform.is_valid():
            updateform.save()
            return redirect('Home')

    return render(request, 'update_profile_page.html', {'staffs':staffs, 'updateform':updateform} )


def delete_profile(request, pk):
    staffs = Staffs_profile.objects.get(id = pk)
    if request.method == 'POST':
        staffs.delete()
        return redirect('Home')
    return render(request, 'delete_profile.html' )

def Staffprofile(request,pk):
   staff = Staffs_profile.objects.get(id=pk)
   return render(request, 'profile_page.html', {'staff':staff})