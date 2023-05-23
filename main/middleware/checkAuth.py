from django.http import HttpResponseRedirect
from main.models import Profile
from django.shortcuts import render, get_object_or_404
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            if "/post/" in request.path and not get_object_or_404(Profile, user=request.user.id).group:
                return HttpResponseRedirect('/')
            elif "/admin/" in request.path:
                return None
        elif '/login/' or '/registration/' in request.path:
            return None
        else:
            return HttpResponseRedirect('/login/')