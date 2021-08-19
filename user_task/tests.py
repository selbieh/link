from django.contrib.auth.models import User, Group, Permission
from django.db.models import Q
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestTaskView(APITestCase):

    def setUp(self) -> None:
        self.end_user = User.objects.create_user(
            username="end_user",
            password='strongpassword'
        )
        self.end_user_token = Token.objects.create(user=self.end_user)
        self.admin_user = User.objects.create_user(
            username="admin_user",
            password='strongpassword'
        )
        self.admin_user_token = Token.objects.create(user=self.admin_user)
        self.admin_group = Group.objects.create(name='Admin')
        self.admin_group.permissions.set(
            Permission.objects.filter(
                Q(codename='add_task') |
                Q(codename='delete_task') |
                Q(codename='change_task')

            ))
        self.admin_user.groups.set([self.admin_group])

    def test_not_authed_user_create_task(self):
        response=self.client.post(reverse('task-list'))
        self.assertEqual(response.status_code,401)

    def test_end_user_create_task(self):
        response=self.client.post(reverse('task-list'), HTTP_AUTHORIZATION='Token {}'.format(self.end_user_token.key))
        self.assertEqual(response.status_code,403)

    def test_end_user_admin_user(self):
        data={
            "status":"finished",
            "due_date":"2020-03-12T12:05",
            "assigned_to": 1

        }
        response = self.client.post(reverse('task-list'),data=data, HTTP_AUTHORIZATION='Token {}'.format(self.admin_user_token.key))
        self.assertEqual(response.status_code, 201)

    def test_filtered_task(self):
        data = {
            "status": "finished",
            "due_date": "2020-03-12T12:05",
            "assigned_to": 1

        }
        response = self.client.post(reverse('task-list'), data=data,
                                    HTTP_AUTHORIZATION='Token {}'.format(self.admin_user_token.key))
        self.assertEqual(response.status_code, 201)
        data = {
            "status": "finished",
            "due_date": "2020-03-12T12:05",
            "assigned_to": 2

        }
        response = self.client.post(reverse('task-list'), data=data,
                                    HTTP_AUTHORIZATION='Token {}'.format(self.admin_user_token.key))
        self.assertEqual(response.status_code, 201)

        #admin
        response = self.client.get(reverse('task-list'),
                                    HTTP_AUTHORIZATION='Token {}'.format(self.admin_user_token.key))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 2)
        #end_user
        response = self.client.get(reverse('task-list'),
                                   HTTP_AUTHORIZATION='Token {}'.format(self.end_user_token.key))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)

