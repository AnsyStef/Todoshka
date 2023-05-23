from django.shortcuts import render, get_object_or_404
from .forms import *
from django.http import HttpResponseRedirect
from .models import Profile, Group, Note, Setting
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from Todoshka import settings
import os
from django.template import *

# <------ LOGIN ------>
class AUTHENTICATION:
    def Logout(request):
        logout(request)
        return HttpResponseRedirect('/')

    def Registration(request):

        if request.method == "POST":
            try:
                form = LoginForm(request.POST)
                if form.is_valid():

                    print('form valid')
                    name = form.cleaned_data.get("email")
                    word = form.cleaned_data.get('password')
                    email, name = name, name.split("@")[0]

                    try:
                        user = User.objects.create_user(username=name, password=word).save
                        try:
                            user = authenticate(request, username=name, password=word)
                        except Exception as e:
                            print(e)
                        login(request, user)
                        user = get_object_or_404(User, username=name)
                        Profile.objects.create(user=user, password=word).save
                        Setting.objects.create(user=user).save
                        return HttpResponseRedirect('/')

                    except Exception as e:
                        print(e)
                        return HttpResponseRedirect(f'/registration/?error={e}/')
            except Exception as e:
                print(e)
                return HttpResponseRedirect(f'/registration/?error={e}/')
            return HttpResponseRedirect('/')
        else:
            loginForm = LoginForm(request.POST)
            return render(request, 'auth/registration.html', context={'form': loginForm})

    def Login(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            print(request.POST['email'] + "+" + request.POST['password'])
            try:
                    username = request.POST['email']
                    password = request.POST['password']
                    user = authenticate(request, username=username, password=password)
                    try:
                        login(request, user)
                        print('user authenticated')
                        return HttpResponseRedirect('/')
                    except Exception as e:
                        print(f'user not authenticated with error: {e}')
                        return HttpResponseRedirect('/login/')
            except Exception as e:
                print(f'form is not valid with error: {e}')
                return HttpResponseRedirect('/login/')
        else:
            loginForm = LoginForm(request.POST)
            return render(request, 'auth/login.html', context={'form': loginForm})

# <------ SETTINGS ------>
def Settings(request, username):
    form = UserChangeForm(request.POST)
    if '?changedata' in request.get_full_path():
        if request.method == 'POST':
            name = request.POST['username']
            password = request.POST['password']
            
            print(User.objects.filter(username=name).count())
            if User.objects.filter(username=name).count() == 0:
                user = get_object_or_404(User, username=request.user.username)
                profile = get_object_or_404(Profile, user=request.user.id)
                print(password)
                try:
                    if username != '':
                        user.username = name
                except:
                    pass
                try:
                    if password != '':
                        user.password = password
                        profile.password = password
                except:
                    pass
                user.save()
                authenticate(username=username if username != '' else request.user.username, password=password)
            return HttpResponseRedirect('/')
    return render(request, 'main/settings.html', context={'theme': Setting.objects.get(user=request.user.id), 'form': form})

def ChangeTheme(request, username, theme):
    user = Setting.objects.get(user=request.user.id)
    user.theme = theme
    user.save()
    return HttpResponseRedirect(f'/{request.user.username}/settings/')

def ChangeData(request, username):
    pass

#<------ NOTES ------>
class NOTES:
    def NoteList(request):
        note_list = Note.objects.all()
        members_list = []
        user_data = Profile.objects.get(user=request.user.id)

        for member in Profile.objects.filter(group=user_data.group):
            if str(member.group) != '0':
                members_list.append(member.user.username)

        print(Setting.objects.get(user=request.user.id).theme)
        return render(
            request, 'main/index.html', context={
            'note_list' : note_list,
            'members_list': members_list,
            'request_user': user_data.group,
            'theme': Setting.objects.get(user=request.user.id)}
            )

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
            return render(request, 'main/post_new.html', context={'form': form, 'theme': Setting.objects.get(user=request.user.id)})
        
    def ShowNote(request, pk):
        note = get_object_or_404(Note, pk=pk)
        return render(request, 'main/note_detail.html', context={'note': note, 'pk': note.pk, 'theme': Setting.objects.get(user=request.user.id)})

    def DeleteNote(request, pk):
        note = Note.objects.get(pk=pk)
        note.delete()
        return HttpResponseRedirect('/')

    def AcceptNote(request, pk, username):
        note = Note.objects.get(pk=pk)
        note.worker = username
        note.status = '2'
        note.save(update_fields=["worker",'status'])
        return HttpResponseRedirect('/')

    def MyNotes(request, username):
        members_list = []
        user_data = Profile.objects.get(user=request.user.id)
        for member in Profile.objects.filter(group=user_data.group):
            if str(member.group) != '0':
                members_list.append(member.user.username)
        print(members_list)
        note_list = Note.objects.all()
        return render(request, 'main/my_notes.html', context={'note_list' : note_list, 'theme': Setting.objects.get(user=request.user.id), 'members_list': members_list})

    def CompleteNote(request, pk):
        note = get_object_or_404(Note, pk=pk)
        note.status = '3'
        note.save()
        return HttpResponseRedirect('/')

    def CompletedList(request):
        members_list = []
        user_data = Profile.objects.get(user=request.user.id)

        for member in Profile.objects.filter(group=user_data.group):
            if str(member.group) != '0':
                members_list.append(member.user.username)
        print(members_list)
        return render(request, 'main/completed_list.html', context={'note_list' : Note.objects.all(), 'theme': Setting.objects.get(user=request.user.id), 'members_list': members_list})

    def FreeNotes(request):
        members_list = []
        user_data = Profile.objects.get(user=request.user.id)

        for member in Profile.objects.filter(group=user_data.group):
            if str(member.group) != '0':
                members_list.append(member.user.username)
        print(members_list)
        return render(request, 'main/free_notes.html', context={'note_list': Note.objects.filter(worker = 'Нет'), 'theme': Setting.objects.get(user=request.user.id), 'members_list': members_list})


#<------ GROUPS ------>
class GROUP:
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
                return render(request, 'groups/create.html', context={'form': form, 'theme': Setting.objects.get(user=request.user.id)})
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

        return render(request, 'groups/join.html', context={'form': form, 'theme': Setting.objects.get(user=request.user.id)})

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
        return render(request, 'groups/index.html', context={'member_count': member_count, 'members_list': members_list, 'group': group, 'theme': Setting.objects.get(user=request.user.id)})

    def UserDetail(request, id):
        pass

#<--- DEBUG --->

def dropDB(request):
    Note.objects.all().delete()
    return HttpResponseRedirect('/')

def fillDB(request):
    import random
    for i in range(random.randint(20, 100)):
        Note.objects.create(name='Test', description='Test', creator='System', is_public=True).save()
    return HttpResponseRedirect('/')

def pageNotFound(request, exception):
    return render(request, 'main/page404.html')