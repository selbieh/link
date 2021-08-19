from django.contrib import admin
from .models import Task


@admin.register(Task)
class CompetitionAnswerAdmin(admin.ModelAdmin):
    pass
