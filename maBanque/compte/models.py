
from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class Client(models.Model):
    idClient = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Operation(models.Model):
    idOpe = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=20)
    montant = models.IntegerField()
    compte = models.ForeignKey("Compte", on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"{self.date} - {self.montant}"

    

class Compte(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero = models.IntegerField()
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    solde = models.IntegerField(default=0)
    #operations = models.ManyToManyField(Operation)

    def __str__(self):
        return f"{self.numero} - {self.client}"



