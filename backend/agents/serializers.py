from rest_framework import serializers
from projects.models import Task, Project
from users.models import User
import string
import random
from .models import Agent, AgentAPIKey, AgentAction

def generate_shared_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

class AgentActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentAction
        fields = ['id', 'action_type', 'description', 'timestamp']
        read_only_fields = ['id', 'action_type', 'description', 'timestamp']

class AgentAPIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentAPIKey
        fields = ['id', 'key', 'scope', 'expires_at', 'last_used', 'total_actions', 'is_active', 'created_at']
        read_only_fields = ['id', 'key', 'last_used', 'total_actions', 'created_at']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Only show full key if it's the first time it was created (to be implemented via context if needed)
        # We'll just obscure the key for regular listing to be safe
        request = self.context.get('request')
        if request and request.method == 'GET' and ret.get('key'):
            ret['key'] = f"{ret['key'][:4]}...{ret['key'][-4:]}"
        return ret


class AgentSerializer(serializers.ModelSerializer):
    keys = AgentAPIKeySerializer(source='agentapikey_set', many=True, read_only=True)
    recent_actions = serializers.SerializerMethodField()

    class Meta:
        model = Agent
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'keys', 'recent_actions']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_recent_actions(self, obj):
        actions = obj.actions.all().order_by('-timestamp')[:5]
        return AgentActionSerializer(actions, many=True).data

    def create(self, validated_data):
        # Set owner automatically from request
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

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
        AgentAction.objects.create(
            agent=agent,
            action_type='task_updated',
            description=f"Updated task '{task.title}' (Shared ID: {task.shared_id})"
        )
        
        return task
