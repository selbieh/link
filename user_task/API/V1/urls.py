from django.urls import path, include
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'user-task',TaskViewSet,basename='task')

urlpatterns=[
    path('', include(router.urls)),
]