from rest_framework import serializers
from projects.models import Task, Project
from users.models import User
import string
import random

def generate_shared_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

class AgentTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'project', 'title', 'description', 'status', 'due_date', 'shared_id', 'created_at', 'updated_at']
        read_only_fields = ['id', 'shared_id', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Auto-generate a shared ID and link the agent
        validated_data['shared_id'] = generate_shared_id()
        agent = self.context['request'].agent
        validated_data['created_by_agent'] = agent
        
        task = super().create(validated_data)
        
        # Log the action
        from agents.models import AgentAction
        AgentAction.objects.create(
            agent=agent,
            action_type='task_created',
            description=f"Created task '{task.title}' (Shared ID: {task.shared_id})"
        )
        
        return task

    def update(self, instance, validated_data):
        task = super().update(instance, validated_data)
        
        # Log the action
        agent = self.context['request'].agent
        from agents.models import AgentAction
        AgentAction.objects.create(
            agent=agent,
            action_type='task_updated',
            description=f"Updated task '{task.title}' (Shared ID: {task.shared_id})"
        )
        
        return task
