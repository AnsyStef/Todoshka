from django.contrib import admin
from .models import *

admin.site.register(Notes)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'group_password']
    fields = ['group_name', 'group_password']
admin.site.register(Group, GroupAdmin)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','rank']
    fields = ['user', 'group', 'rank','trust_factor']
admin.site.register(Profile, ProfileAdmin)