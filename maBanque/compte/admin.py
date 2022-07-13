from django.contrib import admin
from compte.models import Client, Operation, Compte

# Register your models here.
admin.site.register(Client)
admin.site.register(Operation)
admin.site.register(Compte)