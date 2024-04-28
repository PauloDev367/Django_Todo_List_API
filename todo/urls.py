from django.urls import path, include
from rest_framework import routers
from todo.views import TarefaViewSet, ConcluirTarefa

router = routers.DefaultRouter()
router.register('tarefas', TarefaViewSet,basename='tarefas')
urlpatterns = [
    path('', include(router.urls)),
    path('tarefas/<int:id>', ConcluirTarefa.as_view())
]