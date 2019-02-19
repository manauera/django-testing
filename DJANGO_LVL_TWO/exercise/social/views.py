from django.shortcuts import render
from django.http import HttpResponse
from social.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def users(request):
    all_users = User.objects.order_by('fname')
    dict = {'all_users': all_users}
    return render(request, 'users.html', context=dict)
