from django.urls import path, include
from .router import router
from .views import get_csrf_token, CustomAuthToken, OfferCreateView, ItemOffersList

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/csrf/', get_csrf_token, name='get_csrf'),
    path('api/auth/login/', CustomAuthToken.as_view(), name='login'),
    path('api/offers/create/', OfferCreateView.as_view(), name='offer-create'),
path('api/items/<int:item_id>/offers/', ItemOffersList.as_view(), name='item-offers'),
]
