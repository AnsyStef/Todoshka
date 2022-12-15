from django.shortcuts import render, get_object_or_404
from .forms import ContactForm, LoginForm
from django.http import HttpResponseRedirect
from .models import Notes
from django.core import serializers
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def Registration(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get("username")
                word = form.cleaned_data.get('password')
                try:
                    user = User.objects.create_user(username=name, password=word)
                    user.save()
                except:
                    messages.info(request, 'Что-то пошло не так!')
                    return HttpResponseRedirect('/registration/')
                return HttpResponseRedirect('/login/')
            else:
                return HttpResponseRedirect('/registration/')
        else:
            loginForm = LoginForm(request.POST)
            return render(request, 'main/registration.html', context={'form': loginForm})
    else:
        return HttpResponseRedirect('/')
    
def Login(request):
    if not request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect('/')

def NoteList(request):
    if request.user.is_authenticated:
        note_list = Notes.objects.all()
        return render(request, 'main/index.html', context={'note_list' : note_list})
    else:
        return HttpResponseRedirect('login/')

def PostNote(request, username):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
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
    note_list = Notes.objects.all()
    return render(request, 'main/free_notes.html', context={'note_list' : note_list})




def dropDB(request):
    note_list = Notes.objects.all()
    for note in note_list:
        note.delete()
    return HttpResponseRedirect('/')

def Debug(request):
    return render(request, 'main/debug_panel.html')

def pageNotFound(request, exception):
    return render(request, 'main/page404.html')