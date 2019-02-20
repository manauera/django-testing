from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request, 'app_basic/index.html')


def form_view(request):
    form = forms.TestForm()

    if request.method == 'POST':
        form = forms.TestForm(request.POST)
        if form.is_valid():
            print("Validation complete!")
            print("Name: "+ form.cleaned_data['name'])
            print("Email: "+ form.cleaned_data['email'])
            print("Text: "+ form.cleaned_data['text'])
            
    return render(request, 'app_basic/form.html', {'form':form})
