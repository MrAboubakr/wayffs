from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentTaskViewSet, AgentViewSet, AgentAPIKeyViewSet

router = DefaultRouter()
router.register(r'tasks', AgentTaskViewSet, basename='agent-tasks')

# Dashboards for Users to manage their agents
user_router = DefaultRouter()
user_router.register(r'manage/agents', AgentViewSet, basename='manage-agents')
user_router.register(r'manage/keys', AgentAPIKeyViewSet, basename='manage-keys')

urlpatterns = [
    # Agents API endpoints (for AI Agents)
    path('agents/', include(router.urls)),
    
    # User API endpoints (for managing AI Agents from the frontend dashboard)
    path('users/', include(user_router.urls)),
]
