from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ClothingItem, ExchangeRequest, Offer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']


class ClothingItemSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = ClothingItem
        fields = ['id', 'title', 'description', 'size', 'image', 'is_available', 'owner', 'category']


class ExchangeRequestSerializer(serializers.ModelSerializer):
    requester = UserSerializer(read_only=True)
    requested_item = ClothingItemSerializer(read_only=True)

    class Meta:
        model = ExchangeRequest
        fields = ['id', 'requester', 'requested_item', 'status', 'created_at']


class OfferSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    class Meta:
        model = Offer
        fields = ['id', 'creator', 'item', 'created_at']
        read_only_fields = ['creator', 'created_at']

    def validate(self, data):
        if data['item'].owner == self.context['request'].user:
            raise serializers.ValidationError("Вы не можете создать оффер на свой собственный предмет")
        return data