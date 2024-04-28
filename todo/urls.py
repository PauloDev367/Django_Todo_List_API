from django.urls import path, include
from rest_framework import routers
from todo.views import TarefaViewSet, ConcluirTarefa, ComentariosViewSet

router = routers.DefaultRouter()
router.register('tarefas', TarefaViewSet,basename='tarefas')
router.register('comentarios', ComentariosViewSet,basename='comentarios')

urlpatterns = [
    path('', include(router.urls)),
    path('tarefas/<int:id>', ConcluirTarefa.as_view())
]