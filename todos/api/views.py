from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from todos.models import Todo
from todos.api.serializers import TodoSerializer


class TodoViewSet(ModelViewSet):
  
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
  permission_classes = [AllowAny]