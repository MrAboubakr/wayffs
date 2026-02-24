from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.utils import timezone
from projects.models import Task
from .models import Agent, AgentAPIKey, AgentAction
from .serializers import AgentTaskSerializer, AgentSerializer, AgentAPIKeySerializer
from .permissions import HasAgentAPIKey, AgentNoDeletePermission
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view or edit their AI Agents.
    """
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Agent.objects.filter(owner=self.request.user)

class AgentAPIKeyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to manage API Keys for their Agents.
    """
    serializer_class = AgentAPIKeySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AgentAPIKey.objects.filter(agent__owner=self.request.user)

    def perform_create(self, serializer):
        # Ensure the agent belongs to the user
        agent_id = self.request.data.get('agent')
        try:
            agent = Agent.objects.get(id=agent_id, owner=self.request.user)
            serializer.save(agent=agent)
        except Agent.DoesNotExist:
            raise serializers.ValidationError({"agent": "Invalid agent or permission denied."})

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
