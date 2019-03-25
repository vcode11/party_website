from django.shortcuts import render
from django.http import HttpResponse

from .forms import MemberRegistrationForm

app_name = 'party'

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
        context = {
            'form':form,
            'message':'Thank you for joining us and becoming part of our movement.'
        }
    return render(request,'party/apply.html',context)