from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from projects.models import Task
from .serializers import AgentTaskSerializer
from .permissions import HasAgentAPIKey, AgentNoDeletePermission
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

class AgentTaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AI Agents to view or edit tasks.
    """
    serializer_class = AgentTaskSerializer
    permission_classes = [HasAgentAPIKey, AgentNoDeletePermission]
    
    def get_queryset(self):
        # Only return tasks for projects owned by the agent's owner
        owner = self.request.agent.owner
        return Task.objects.filter(project__owner=owner)

    def perform_create(self, serializer):
        # Update usage tracking
        self.request.agent_key.last_used = timezone.now()
        self.request.agent_key.total_actions += 1
        self.request.agent_key.save()
        
        serializer.save()

    def perform_update(self, serializer):
        # Update usage tracking
        self.request.agent_key.last_used = timezone.now()
        self.request.agent_key.total_actions += 1
        self.request.agent_key.save()
        
        serializer.save()

    @extend_schema(
        summary="List accessible tasks",
        description="Returns all tasks within projects owned by the agent's creator.",
        parameters=[
            OpenApiParameter(name="project", description="Filter by project ID", required=False, type=int),
        ]
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        project_id = request.query_params.get('project', None)
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
            
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
