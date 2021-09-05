from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
from .forms import customForm
from .models import customuser
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form=customForm(request.POST)
        if form.is_valid():          
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('blog-home')

    form=customForm()
    data={
        'form':form
    }
    return render(request,'users/register.html',context=data)
