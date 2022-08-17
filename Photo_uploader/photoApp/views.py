
import imp
from django.shortcuts import render,HttpResponseRedirect
from .forms import *
from .models import uppic
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
# Create your views here.

#homepage
def home(request):
    form = uppic.objects.all()
    pagination=Paginator(form,5)
    page_nums=request.GET.get('page')
    page_obj=pagination.get_page(page_nums)
    return render(request,'web/home.html',{'prof':page_obj})

#sign up form
def signup(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save()
            grp=Group.objects.get(name='perm')
            user.groups.add(grp)
            form=signupform()
            messages.success(request,'Sign up successfully :)')

    else:
        form=signupform()
    return render(request,'web/sign_up.html',{'form':form})

#sign in form
def signin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=signinform(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']

                user=authenticate(username=uname,password=upass)

                if user is not None:
                    login(request,user)
                    messages.success(request,'Welcome ')
                    return HttpResponseRedirect('/home/')

        else:
            form=signinform()

        return render(request,'web/sign_in.html',{'form':form})

    else:
        return HttpResponseRedirect('/home/')

#upload photo
def upphoto(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=newphoto(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                form=newphoto()
                messages.success(request,'Photo Uploaded Successfully :)')

        else:
            upuser=request.user
            form=newphoto(instance=upuser)

        return render(request,'web/upload.html',{'form':form})

    else:
        return HttpResponseRedirect('/signin/')


#profile
def profile(request):   
    if request.user.is_authenticated:
        uname=request.user
        #
        fpic=uppic.objects.filter(username=uname).all()
        return render(request,'web/profile.html',{'prof':fpic,'uname':uname})

    else:
        return HttpResponseRedirect('/signin/')

def deletepic(request,id):
    if request.method=='POST':
        delid=uppic.objects.get(pk=id)
        delid.delete()

    return HttpResponseRedirect('/profile/')

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/signin/')

def about(request):
    return render(request,'web/about.html')

def contact(request):
    if request.method=='POST':
        form=contactpage(request.POST)
        if form.is_valid():
            form.save()
            form=contactpage()
            messages.success(request,'Thank You :)')

    else:
        form=contactpage()

    return render(request,'web/contact.html',{'form':form})