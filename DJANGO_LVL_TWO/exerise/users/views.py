from django.shortcuts import render
from django.http import HttpResponse
from user 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_list(request):
    users = Users.objects.order_by('fname')
    dict = {'users_db': users}
    return render(request, 'users.html', context=dict)
