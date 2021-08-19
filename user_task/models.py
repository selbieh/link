from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    FINISHED = 'finished'
    PENDING = 'pending'
    status_choices = [
        (FINISHED, FINISHED),
        (PENDING, PENDING)
    ]

    """
    task model held the tasks
    N.B: assigned_to is end-user
    created_by: is admin user
    updated_at ,created_at is 
    models.PROTECT to persistence history in database if must delete user should implement soft delete
    """
    title = models.CharField(null=True, blank=True, max_length=125)
    description = models.TextField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, null=False, blank=False, related_name='assigned_tasks',
                                    on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, null=False, blank=False, related_name='created_tasks',
                                   on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=status_choices, max_length=15)
    due_date = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f'{self.title or ""}"  assigned to " {self.assigned_to}'
