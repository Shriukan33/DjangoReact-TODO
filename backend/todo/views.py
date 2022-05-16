from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo


# The viewsets base class provides the implementation for CRUD operations
# by default.
class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
