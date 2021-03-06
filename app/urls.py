from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import Check, Register, main, delete_user, all
from django.conf.urls.static  import static
from django.conf import settings

urlpatterns = [
    path('', main, name='main'),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', Register),
    path('check-token/', Check),
    path('delete/<int:id>/', delete_user, name='delete'),
    path('all/', all),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
