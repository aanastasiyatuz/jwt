from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from rest_framework.decorators import api_view
from django.shortcuts import render

def main(request):
    users = get_user_model().objects.all()
    return render(request, 'base.html', locals())

@api_view(["POST"])
def Register(request):
    User = get_user_model()
    un = request.POST.get("username")
    pw = request.POST.get("password")
    if un and pw:
        if User.objects.filter(username=un).exists():
            return HttpResponseBadRequest("user with such 'username' already exists")
        User.objects.create_user(username=un, password=pw)
        return HttpResponse("successfully signed up!")
    return HttpResponseForbidden("use form-data\nor 'username' and 'password' is required")

@api_view(["GET"])
def Check(request):
    if request.user.is_authenticated: return HttpResponse("using token")
    return HttpResponseForbidden("token invalid or expired")