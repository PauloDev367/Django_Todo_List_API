from rest_framework import serializers
from todo.models import Tarefa, Comentarios


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ('id', 'titulo', 'descricao', 'concluida', 'data_conclusao')
        
class ComentarioInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ('id', 'tarefa', 'descricao')

class ComentarioOutputSerializer(serializers.ModelSerializer):
    tarefa = serializers.ReadOnlyField(source='tarefa.titulo')
    class Meta:
        model = Comentarios
        fields = ('id', 'tarefa', 'descricao')