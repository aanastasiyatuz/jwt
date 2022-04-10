from django.contrib.auth import get_user_model
from django.http import HttpResponse, Http404

def Register(request):
    if request.method == 'POST':
        User = get_user_model()
        user = User.objects.create_user(username=request.POST.get("username"), password=request.POST.get("password"))
        return HttpResponse("successfully signed up!")
