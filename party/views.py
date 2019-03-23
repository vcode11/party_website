from django.shortcuts import render
from django.http import HttpResponse

from .forms import MemberRegistrationForm

def home(request):
    return render(request,'party/base.html',{})
    
def apply(request):
    if request.method == 'GET':
        form = MemberRegistrationForm()
        context = {
            'form':form,
        }
    else:
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['dob'])
            print(form.cleaned_data['email'])
        context = {
            'form':form,
        }
    return render(request,'party/apply.html',context)