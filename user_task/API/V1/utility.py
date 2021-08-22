from django_filters import rest_framework as filters
from user_task.models import Task
# 'assigned_to', 'created_by','created_at','status','due_date'
class TaskFilter(filters.FilterSet):
    assigned_to = filters.NumberFilter(field_name='assigned_to')
    created_by = filters.NumberFilter(field_name='created_by_id')
    created_at__lt = filters.DateTimeFilter(field_name='created_at', lookup_expr='lt')
    created_at__gt = filters.DateTimeFilter(field_name='created_at', lookup_expr='gt')
    due_date__gt = filters.DateTimeFilter(field_name='created_at', lookup_expr='gt')
    due_date__lt = filters.DateTimeFilter(field_name='created_at', lookup_expr='lt')
    status = filters.CharFilter(field_name='status')

    class Meta:
        model = Task
        fields = ['assigned_to', 'created_by', 'created_at', 'due_date','status']

