
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from user_task.API.V1.serializers import TaskSerializer
from user_task.models import Task
from user_task.API.V1.utility import TaskFilter
from django_filters import rest_framework as filters




class TaskViewSet(ModelViewSet):
    """
    status options ["finished" , "pending"]
    """
    serializer_class = TaskSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilter
    def get_queryset(self):
        if self.request.user.groups.filter(name="Admin"):
            return Task.objects.all().order_by('-id')
        else:
            return Task.objects.filter(assigned_to=self.request.user).order_by('-id')
