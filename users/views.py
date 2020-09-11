from django.shortcuts import render,redirect
from .forms import CreateUserForm,UserUpdateForm,StudentUpdateForm
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import Tutor, Student
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@unauthenticated_user
def RegisterOption(request):
    title = "Register Option"
    return render(request, "users/register_option.html",{'title':title})

@unauthenticated_user
def StudentRegister(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='students')
            user.groups.add(group)

            Student.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'users/studentregister.html', context)

@unauthenticated_user
def TutorRegister(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='colleges')
            user.groups.add(group)

            Tutor.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'users/tutor_register.html', context)

def logoutUser(request):
	logout(request)
	return redirect('/')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        sp_form = StudentUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.student)
        if u_form.is_valid() and sp_form.is_valid():
            u_form.save()
            sp_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('student_profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        sp_form = StudentUpdateForm(instance=request.user.student)

    context = {
        'u_form': u_form,
        'sp_form': sp_form
    }

    return render(request, 'e-learning/student_update.html',context)