from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.NoteList),
    path('postnew/', views.PostNote),
    path('debugtools/dropdb/', views.dropDB),
    path('debugtools/filldb/', views.fillDB),
    path('note/<pk>/', views.ShowNote, name='note_detail'),
    path('note/<pk>/delete/', views.DeleteNote, name='note_delete'),
    path('note/<pk>/accept/<username>/', views.AcceptNote, name='note_accept'),
    path('post/<username>/', views.PostNote, name='post'),
    path('<username>/notes/', views.MyNotes, name='my_notes'),
    path('note/<pk>/complete/', views.CompleteNote, name='complete'),
    path('notes/completed/', views.CompletedList, name='completed'),
    path('notes/free/', views.FreeNotes),
    path('login/', views.Login, name='login'),
    path('registration/', views.Registration, name='reg'),
    path('logout/', views.Logout, name='logout'),
    path('group/pk=<pk>/', views.GroupIndex, name='group'),
    path('group/create/', views.GroupCreate, name='group_create'),
    path('group/join/', views.GroupJoin, name='group_join'),
    path('group/<pk>/leave/', views.GroupLeave, name='group_leave'),
    path('group/u=<id>/', views.UserDetail, name='user_detail'),
]