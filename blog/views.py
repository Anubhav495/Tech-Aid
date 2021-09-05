from django.shortcuts import render
from django.http import HttpResponse
from .models import postblog
# Create your views here.

def home(request):
    Post={
        "posts":postblog.objects.all()
    }
    return render(request,'blog/home.html',context=Post);

def about(request):
    return render(request,'blog/about.html');