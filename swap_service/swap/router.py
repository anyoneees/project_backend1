from rest_framework import routers
from .views import ClothingItemViewSet, ExchangeRequestViewSet

router = routers.DefaultRouter()
router.register(r'clothing-items', ClothingItemViewSet)
router.register(r'exchange-requests', ExchangeRequestViewSet)
