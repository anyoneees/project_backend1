from django.urls import path, include
from .router import router
from .views import get_csrf_token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/csrf/', get_csrf_token, name='get_csrf'),
    path('api/auth/login/', obtain_auth_token, name='login'),
]
