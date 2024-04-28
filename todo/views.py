from rest_framework import viewsets, generics
from todo.models import Tarefa, Comentarios
from rest_framework.response import Response
from todo.serializers import TarefaSerializer, ComentarioInputSerializer, ComentarioOutputSerializer

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
    
class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    def get_serializer_class(self):
        # se for um método de listar todos (list) ou buscar um detalhado (retrieve) eleusa o output 
        if self.action == 'list' or self.action == 'retrieve':
            return ComentarioOutputSerializer
        else:
            return ComentarioInputSerializer