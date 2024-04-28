from django.urls import path, include
from rest_framework import routers
from todo.views import TarefaViewSet

router = routers.DefaultRouter()
router.register('tarefas', TarefaViewSet,basename='tarefas')
urlpatterns = [
    path('', include(router.urls)),
]