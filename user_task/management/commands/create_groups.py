from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand
from django.db.models import Q


class Command(BaseCommand):
    help = "creat default groups"

    def handle(self, *args, **options):
        group,created=Group.objects.get_or_create(name='Admin')
        group.permissions.set(
            Permission.objects.filter(
                Q(codename='add_task') |
                Q(codename='delete_task') |
                Q(codename='change_task')

            ))
