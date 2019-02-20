from django.shortcuts import render
from django.http import HttpResponse
from social.models import User
from social import forms

# Create your views here.
def index(request):
    return render(request, 'social/index.html')

def users(request):
    all_users = User.objects.order_by('fname')
    dict = {'all_users': all_users}
    return render(request, 'social/users.html', context=dict)

def register(request):
    form_data = forms.UserRegisterForm()
    if request.method == 'POST':
        form_data = forms.UserRegisterForm(request.POST)
        if form_data.is_valid():
            User.objects.get_or_create(fname=form_data.cleaned_data['fname'], lname=form_data.cleaned_data['lname'], email=form_data.cleaned_data['email'])

    return render(request, 'social/register.html', {'form':form_data})
