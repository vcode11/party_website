from django.shortcuts import render
from django.http import HttpResponse

from .forms import MemberRegistrationForm
from .models import Member, State, District

app_name = 'party'

def home(request):
    return render(request,'party/base.html',{})

def apply(request):
    if request.method == 'GET':
        form = MemberRegistrationForm()
        context = {
            'form':form,
        }
        return render(request,'party/apply.html',context)
    else:
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            member = Member(
                            name=data['name'], 
                            dob=data['dob'], 
                            gender=data['gender'],
                            email=data['email'],
                            phone=data['phone_number'],
                            state=data['state'].name,
                            district=data['district'].name,
                            address=data['address'],
                            pincode = data['pin_code'],
                            voterID = data['voterId'],
                        )
            member.save()
            context = {
                'form':form,
                'message':'Thank you for joining us and becoming part of our movement.'
            }
            return render(request,'party/apply.html',context)
        return render(request,'party/apply.html',{'form':form})