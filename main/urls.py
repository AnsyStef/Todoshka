from django.urls import path, include
from . import views

urlpatterns = [
# <------ AUTHENTICATION ------>
    path('login/', views.AUTHENTICATION.Login, name='login'),
    path('registration/', views.AUTHENTICATION.Registration, name='reg'),
    path('logout/', views.AUTHENTICATION.Logout, name='logout'),
# <------ NOTES ------>
    path('', views.NOTES.NoteList),
    path('postnew/', views.NOTES.PostNote),
    path('note/<pk>/', views.NOTES.ShowNote, name='note_detail'),
    path('note/<pk>/delete/', views.NOTES.DeleteNote, name='note_delete'),
    path('note/<pk>/accept/<username>/', views.NOTES.AcceptNote, name='note_accept'),
    path('post/<username>/', views.NOTES.PostNote, name='post'),
    path('<username>/notes/', views.NOTES.MyNotes, name='my_notes'),
    path('note/<pk>/complete/', views.NOTES.CompleteNote, name='complete'),
    path('notes/completed/', views.NOTES.CompletedList, name='completed'),
    path('notes/free/', views.NOTES.FreeNotes),
# <------ GROUP ------>
    path('group/pk=<pk>/', views.GROUP.GroupIndex, name='group'),
    path('group/create/', views.GROUP.GroupCreate, name='group_create'),
    path('group/join/', views.GROUP.GroupJoin, name='group_join'),
    path('group/<pk>/leave/', views.GROUP.GroupLeave, name='group_leave'),
    path('group/u=<id>/', views.GROUP.UserDetail, name='user_detail'),
# <------ SETTINGS ------>
    path('<username>/settings/', views.Settings, name='settings'),
    path('<username>/settings/?changetheme=<theme>', views.ChangeTheme, name='changeTheme'),
]