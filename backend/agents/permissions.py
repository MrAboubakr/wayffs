from rest_framework.permissions import BasePermission
from .models import AgentAPIKey, AgentAction

class HasAgentAPIKey(BasePermission):
    """
    Allows access only to requests with a valid Agent API Key.
    """
    def has_permission(self, request, view):
        api_key = request.headers.get('Authorization')
        
        if not api_key:
            return False
            
        # Expecting format: "Api-Key <key>"
        parts = api_key.split()
        if len(parts) != 2 or parts[0] != 'Api-Key':
            return False
            
        key_value = parts[1]
        
        try:
            agent_key = AgentAPIKey.objects.get(key=key_value, is_active=True)
            
            # Check expiration
            if agent_key.is_expired:
                return False
                
            # Attach agent to request for later use
            request.agent = agent_key.agent
            request.agent_key = agent_key
            
            return True
            
        except AgentAPIKey.DoesNotExist:
            return False

class AgentNoDeletePermission(BasePermission):
    """
    Prevents any DELETE requests from Agents.
    """
    def has_permission(self, request, view):
        # Already authenticated an agent
        if getattr(request, 'agent', None):
            if request.method == 'DELETE':
                return False
                
            # Check scope if needed
            agent_key = getattr(request, 'agent_key', None)
            if agent_key and agent_key.scope == 'read_only' and request.method not in ['GET', 'HEAD', 'OPTIONS']:
                return False
                
        return True
