from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ClothingItem, ExchangeRequest
from .serializers import ClothingItemSerializer, ExchangeRequestSerializer
from django.middleware.csrf import get_token
from django.http import JsonResponse

def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})


class ClothingItemViewSet(viewsets.ModelViewSet):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def request_exchange(self, request, pk=None):
        item = self.get_object()
        if not item.is_available:
            return Response({'error': 'Item is not available'}, status=400)
        ExchangeRequest.objects.create(requester=request.user, requested_item=item)
        return Response({'status': 'Exchange request sent'})


class ExchangeRequestViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRequest.objects.all()
    serializer_class = ExchangeRequestSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return super().get_queryset().filter(requested_item__owner=self.request.user)

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        exchange_request = self.get_object()
        exchange_request.status = 'accepted'
        exchange_request.save()
        return Response({'status': 'Exchange request accepted'})

    @action(detail=True, methods=['post'])
    def decline(self, request, pk=None):
        exchange_request = self.get_object()
        exchange_request.status = 'declined'
        exchange_request.save()
        return Response({'status': 'Exchange request declined'})
