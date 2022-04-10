from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseForbidden
from rest_framework.decorators import api_view

def Register(request):
    if request.method == 'POST':
        User = get_user_model()
        User.objects.create_user(username=request.POST.get("username"), password=request.POST.get("password"))
        return HttpResponse("successfully signed up!")

@api_view(["GET"])
def Check(request):
    if request.user.is_authenticated: return HttpResponse("using token")
    return HttpResponseForbidden("token invalid or expired")