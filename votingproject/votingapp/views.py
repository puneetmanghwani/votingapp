from django.shortcuts import render
from votingapp.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from votingapp.models import Visited,Items
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'votingapp/index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'votingapp/login.html',{'loginfailed':True})
    else:
        return render(request, 'votingapp/login.html',{'loginfailed':False})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            name_person = user_form.cleaned_data['username']
            person_id = User.objects.get(username=name_person)  
            visitedperson = Visited(user_name=person_id,voted=False)
            visitedperson.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'votingapp/register.html',
                          {'user_form':user_form,
                           'registered':registered})

@login_required
def voting(request):
    if request.method == 'POST':
        userloggedin = request.user.username
        vot_obj=Visited.objects.get(user_name=userloggedin)
        if vot_obj.voted==False:
            itemgot=request.POST.get('action')
            obj,created = Items.objects.get_or_create(ItemName=itemgot)
            if(obj.ItemCount==None):
                obj.ItemCount=1
            else:
                obj.ItemCount+=1;
            obj.save()
            vot_obj.voted=True
            vot_obj.save()
            return HttpResponse("VOTE SUBMITTED")
        else:
            return HttpResponse("You can only vote once")
    else:
        return render(request,'votingapp/voting.html')


 
    