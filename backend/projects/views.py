from rest_framework import viewsets, permissions, status, decorators
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Project, Task, Comment
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(Q(owner=user) | Q(followers=user)).distinct()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @decorators.action(detail=False, methods=['post'])
    def track(self, request):
        track_id = request.data.get('track_id')
        if not track_id:
            return Response({'error': 'Track ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        project = get_object_or_404(Project, track_id=track_id)
        if project.owner == request.user:
            return Response({'error': 'You cannot track your own project'}, status=status.HTTP_400_BAD_REQUEST)
        
        project.followers.add(request.user)
        return Response(ProjectSerializer(project, context={'request': request}).data)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Return tasks for projects owned or followed by user
        return Task.objects.filter(
            Q(project__owner=user) | Q(project__followers=user)
        ).distinct()

    def perform_create(self, serializer):
        project = serializer.validated_data['project']
        if project.owner != self.request.user:
            raise permissions.PermissionDenied("Only project owner can create tasks")
        serializer.save()

    def perform_update(self, serializer):
        if serializer.instance.project.owner != self.request.user:
            raise permissions.PermissionDenied("Only project owner can update tasks")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.project.owner != self.request.user:
            raise permissions.PermissionDenied("Only project owner can delete tasks")
        instance.delete()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter comments by task if provided
        queryset = Comment.objects.all()
        task_id = self.request.query_params.get('task')
        if task_id:
            queryset = queryset.filter(task_id=task_id)
        
        # Ensure user has access to the project
        user = self.request.user
        return queryset.filter(
            Q(task__project__owner=user) | Q(task__project__followers=user)
        ).distinct()

    def perform_create(self, serializer):
        task = serializer.validated_data['task']
        user = self.request.user
        if task.project.owner != user and not task.project.followers.filter(id=user.id).exists():
             raise permissions.PermissionDenied("You do not have access to this project")
        serializer.save(author=user)
