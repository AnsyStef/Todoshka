from django.urls import path
from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.NoteList),
    path('postnew/', views.PostNote),
    path('debugtools/dropdb/', views.dropDB),
    path('note/<pk>/', views.ShowNote, name='note_detail'),
    path('note/<pk>/delete/', views.DeleteNote, name='note_delete'),
    path('note/<pk>/accept/<username>/', views.AcceptNote, name='note_accept'),
    path('post/<username>/', views.PostNote, name='post'),
    path('<username>/notes/', views.MyNotes, name='my_notes'),
    path('note/<pk>/complete/', views.CompleteNote, name='complete'),
    path('notes/completed/', views.CompletedList, name='completed'),
    path('notes/free/', views.FreeNotes, name='free'),
    path('login/', views.Login, name='login'),
    path('registration/', views.Registration, name='reg'),
    path('logout/', views.Logout, name='logout'),
    path('debugtools/', views.Debug, name='debug'),
]