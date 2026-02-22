from django.contrib import admin
from .models import Agent, AgentAPIKey, AgentAction

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    search_fields = ('name', 'owner__email', 'owner__username')

@admin.register(AgentAPIKey)
class AgentAPIKeyAdmin(admin.ModelAdmin):
    list_display = ('agent', 'scope', 'expires_at', 'is_active', 'total_actions')
    list_filter = ('scope', 'is_active')
    readonly_fields = ('key', 'created_at', 'last_used', 'total_actions')

@admin.register(AgentAction)
class AgentActionAdmin(admin.ModelAdmin):
    list_display = ('agent', 'action_type', 'timestamp')
    list_filter = ('action_type', 'timestamp')
    readonly_fields = ('agent', 'action_type', 'description', 'timestamp')
