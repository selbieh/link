from django.contrib.auth.models import User
from rest_framework import serializers

from user_task.models import Task


class TaskSerializer(serializers.ModelSerializer):

    """
    created by will auto captured from request (no need to send by FE)
    """
    created_by = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all(),
                                              default=serializers.CurrentUserDefault())
    class Meta:
        fields = '__all__'
        model = Task
