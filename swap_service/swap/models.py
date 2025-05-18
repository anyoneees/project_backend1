from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class ClothingItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clothing_items')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='clothing_images/')
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Offer(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers_created')
    item = models.ForeignKey('ClothingItem', on_delete=models.CASCADE, related_name='offers_received')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Offer #{self.id} by {self.creator.username} for {self.item.title}"


class ExchangeRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requested_exchanges')
    requested_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE, related_name='exchange_requests')
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
