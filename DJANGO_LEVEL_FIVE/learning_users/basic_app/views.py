from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):

    registered = False

    if request.method == 'GET':
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    else:
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'basic_app/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('password')

        user = authenticate(username=un, password=pw)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active! :(')
        else:
            print("Tried to login and failed!")
            print("Username: {} and password: {}".format(un, pw))
            return HttpResponse("Invalid login details!")
    else:
        return render(request, 'basic_app/login.html')

    return render(request, 'basic_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def other(request):
    return HttpResponse('you are logged in!')
