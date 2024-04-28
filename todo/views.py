from rest_framework import viewsets, generics
from todo.models import Tarefa
from rest_framework.response import Response
from todo.serializers import TarefaSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    
class ConcluirTarefa(generics.ListAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    
    def patch(self,request, *args, **kwargs):
        tarefa = Tarefa.objects.filter(id=kwargs['id']).first()
        if tarefa is None:
            return Response({'error': 'Tarefa não encontrada'}, status=404)
        
        tarefa.concluida = not tarefa.concluida
        tarefa.save()
        
        serializer = self.get_serializer(tarefa)
        return Response(serializer.data)