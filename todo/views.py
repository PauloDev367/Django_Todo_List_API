from rest_framework import viewsets
from todo.models import Tarefa
from todo.serializers import TarefaSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer