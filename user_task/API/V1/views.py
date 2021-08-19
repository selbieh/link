from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from user_task.API.V1.serializers import TaskSerializer
from user_task.models import Task


class TaskViewSet(ModelViewSet):
    """
    status options ["finished" , "pending"]
    """
    serializer_class = TaskSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        if self.request.user.groups.filter(name="Admin"):
            return Task.objects.all().order_by('-id')
        else:
            return Task.objects.filter(assigned_to=self.request.user).order_by('-id')
