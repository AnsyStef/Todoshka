from django.shortcuts import render, get_object_or_404
from .forms import ContactForm, LoginForm, GroupForm
from django.http import HttpResponseRedirect
from .models import Notes, Profile, Group
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from Todoshka import settings
import os

# <------ LOGIN ------>
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def Registration(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("username")
            word = form.cleaned_data.get('password')
            try:
                Profile.objects.create(user=User.objects.create_user(username=name, password=word)).save
            except:
                messages.info(request, 'Что-то пошло не так!')
                return HttpResponseRedirect('/registration/')
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/registration/')
    else:
        loginForm = LoginForm(request.POST)
        return render(request, 'main/registration.html', context={'form': loginForm})
    
def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login/')
    else:
        loginForm = LoginForm(request.POST)
        return render(request, 'main/login.html', context={'form': loginForm})


#<------ NOTES ------>

def NoteList(request):
    note_list = Notes.objects.all()
    members_list = []
    user_data = Profile.objects.get(user=request.user.id)
    for member in Profile.objects.filter(group=user_data.group):
        if str(member.group) != '0':
            members_list.append(member.user.username)
    print(members_list)
    return render(request, 'main/index.html', context={'note_list' : note_list, 'members_list': members_list})

def PostNote(request, username):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(request.path)
    else:
        form = ContactForm(initial={'creator': username})
        return render(request, 'main/post_new.html', context={'form': form})
    
def ShowNote(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    return render(request, 'main/note_detail.html', context={'note': note, 'pk': note.pk})

def DeleteNote(request, pk):
    note = Notes.objects.get(pk=pk)
    note.delete()
    return HttpResponseRedirect('/')

def AcceptNote(request, pk, username):
    note = Notes.objects.get(pk=pk)
    note.worker = username
    note.status = 'Выполняется'
    note.save(update_fields=["worker",'status'])
    return HttpResponseRedirect('/')

def MyNotes(request, username):
    note_list = Notes.objects.all()
    return render(request, 'main/my_notes.html', context={'note_list' : note_list})

def CompleteNote(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.status = f'Выполнено ({datetime.now().date()})'
    note.save()
    return HttpResponseRedirect('/')

def CompletedList(request):
    note_list = Notes.objects.all()
    return render(request, 'main/completed_list.html', context={'note_list' : note_list})

def FreeNotes(request):
    return render(request, 'main/free_notes.html', context={'note_list' : Notes.objects.filter(worker = False)})


#<------ GROUPS ------>

def GroupCreate(request):
    if not get_object_or_404(Profile, user=request.user.id).group:
        form = GroupForm()
        if request.method == 'POST':
            form = GroupForm(request.POST)
            if form.is_valid:
                try:
                    Group.objects.get(group_name=request.POST["group_name"])
                    return HttpResponseRedirect('/group/create/')
                except:
                    Group.objects.create(group_name=request.POST["group_name"], group_password=request.POST["group_password"]).save()
                    return HttpResponseRedirect(f'/group/pk={Group.objects.get(group_name=request.POST["group_name"]).pk}')
            else:
                return HttpResponseRedirect('/group/create/')
        else:
            return render(request, 'groups/create.html', context={'form': form})
    else:
        return HttpResponseRedirect(f'/group/join/')

def GroupJoin(request):
    if not get_object_or_404(Profile, user=request.user.id).group:
        form = GroupForm()
        if request.method == 'POST':
            form = GroupForm(request.POST)
            if form.is_valid:
                if str(Group.objects.get(group_name=request.POST['group_name']).group_password) == str(request.POST['group_password']):
                    user_obj = get_object_or_404(Profile, user=request.user.id)
                    user_obj.group = Group.objects.get(group_name=request.POST['group_name']).pk
                    user_obj.save()
                    return HttpResponseRedirect(f'/group/pk={get_object_or_404(Profile, user=request.user.id).group}/')
    else:
        return HttpResponseRedirect(f'/group/pk={get_object_or_404(Profile, user=request.user.id).group}/')

    return render(request, 'groups/join.html', context={'form': form})

def GroupLeave(request, pk):
    profile = Profile.objects.get(user=request.user.id)
    profile.group = 0
    profile.rank = 'Пользователь'
    profile.save()
    return HttpResponseRedirect('/')

def GroupIndex(request, pk):
    from django.db.models import Count
    member_count = Profile.objects.filter(group=str(pk)).count()
    members_list = []
    for member in Profile.objects.all():
        if str(member.group) == str(pk):
            members_list.append(member)
    group = Group.objects.get(pk=pk)
    return render(request, 'groups/index.html', context={'member_count': member_count, 'members_list': members_list, 'group': group})

def UserDetail(request, id):
    pass

#<--- DEBUG --->

def dropDB(request):
    Notes.objects.all().delete()
    return HttpResponseRedirect('/')

def fillDB(request):
    import random
    for i in range(random.randint(20, 100)):
        Notes.objects.create(name='Test', description='Test', creator='System', is_public=True).save()
    return HttpResponseRedirect('/')

def pageNotFound(request, exception):
    return render(request, 'main/page404.html')