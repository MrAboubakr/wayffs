from django.db import models
from django.conf import settings
from django.utils import timezone
import os
import binascii

def generate_api_key():
    return binascii.hexlify(os.urandom(20)).decode()

class Agent(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='agents')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.owner})"

class AgentAPIKey(models.Model):
    SCOPE_CHOICES = [
        ('all', 'Read/Write (No Delete)'),
        ('read_only', 'Read Only'),
        ('comment_only', 'Comment Only')
    ]

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='api_keys')
    key = models.CharField(max_length=128, unique=True, default=generate_api_key, db_index=True)
    scope = models.CharField(max_length=20, choices=SCOPE_CHOICES, default='all')
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    last_used = models.DateTimeField(null=True, blank=True)
    total_actions = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Key for {self.agent.name} (Expires: {self.expires_at.date()})"

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at

class AgentAction(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='actions')
    action_type = models.CharField(max_length=50)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.agent.name} - {self.action_type} at {self.timestamp}"
