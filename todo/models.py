from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=255,null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    concluida = models.BooleanField(default=False)
    data_conclusao = models.DateField(null=True)

class Comentarios(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)
    descricao = models.TextField()