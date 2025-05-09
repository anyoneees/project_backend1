from django.urls import path, include
from .router import router
from .views import get_csrf_token

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
    path('api/csrf/', get_csrf_token, name='get_csrf'),
]
