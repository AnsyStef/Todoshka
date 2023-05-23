from django.contrib import admin
from .models import *

admin.site.register(Note)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'group_password']
    fields = ['group_name', 'group_password']
admin.site.register(Group, GroupAdmin)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','rank']
    fields = ['user', 'group', 'rank', 'password']
admin.site.register(Profile, ProfileAdmin)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['user','theme']
admin.site.register(Setting, SettingAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['email']
    fields = ['email', 'password']