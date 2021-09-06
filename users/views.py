from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import customForm

# Create your views here.
from django.contrib import messages

def register(request):
    form=customForm()
    data={}
    if request.method == 'POST':
        form=customForm(request.POST)
        if form.is_valid():          
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('blog-home')
        else:
            data=form.errors.as_data()


    data['form']=form
    if 'username' in data:
        for x in data['username']:
            for y in x:
                messages.add_message(request,messages.WARNING,f'{y}')
    if 'password2' in data:
        messages.add_message(request,messages.WARNING,"Password should be atleast 8 characters long. Password should not be all numeric")
    

    return render(request,'users/register.html',context=data)

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request,username=username, password=password)
        if user is not None:
            
            return redirect('blog-home')
    return render(request,'users/login.html')

@login_required
def profile(request):
    return render(request,'users/profile.html')
