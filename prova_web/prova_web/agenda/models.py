from django.db import models

# Create your models here.
class Agenda(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    endereco = models.TextField(max_length=100)

    def __str__(self):
        return self.nome