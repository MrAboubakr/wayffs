from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentTaskViewSet

router = DefaultRouter()
router.register(r'tasks', AgentTaskViewSet, basename='agent-tasks')

urlpatterns = [
    path('agents/', include(router.urls)),
]
