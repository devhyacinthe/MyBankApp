
from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class Client(models.Model):
    idClient = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)

class Operation(models.Model):
    date = models.DateTimeField()
    type = models.CharField(max_length=20)
    montant = models.IntegerField()

class Compte(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero = models.IntegerField()
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    solde = models.IntegerField()
    operations = models.ForeignKey("Operation", on_delete=models.CASCADE)


