from django.http import HttpResponseRedirect
from main.models import Profile
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            if int(Profile.objects.get(user=request.user.id).trust_factor) >= 20 or request.path == '/logout/':
                return None
            else:
                if request.path != '/notfound/':
                    return HttpResponseRedirect('/notfound/')
                else:
                  return None
        elif 'debug' in request.path and request.user.username != 'ansys':
            return HttpResponseRedirect('/notfound/')
        else:
            if request.path == '/login/' or request.path == '/registration/' or request.path == '/notfound/' or request.path == '/logout/':
                return None
            else:
                return HttpResponseRedirect('/login/')