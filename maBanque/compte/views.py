from django.http import HttpResponse
from django.shortcuts import redirect, render
from compte.models import Compte, Operation, Client
from django.contrib import messages

# Create your views here.


def add_client(request):

    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']

        client, _ = Client.objects.get_or_create(nom=nom, prenom=prenom)
        
        client.save()

        messages.success(request, "Client add with success")
        return render(request, "base.html", {"client": client.idClient})
   
        
    return render(request, "compte/add_client.html")


def add_compte(request):

    if request.method == "POST":
        uidclient = request.POST['uidclient']
        client, _ = Client.objects.get_or_create(idClient=uidclient)
        numero = request.POST['numero']

        compte, _ = Compte.objects.get_or_create(numero=numero, client=client)
        compte.save()

        return render(request, "base.html")
    
    return render(request, "compte/add_compte.html")


def add_operation(request):

    try:

        if request.method == "POST":
            numero = request.POST["compte"]
            compte = Compte.objects.get(numero=numero)
            type = request.POST['type']
            montant = int(request.POST['montant'])

            operation, _ = Operation.objects.get_or_create(compte=compte, type=type, montant=montant)
            

            if type == "Retrait":
                if compte.solde >= 0:
                    compte.solde -= montant
                    compte.save()
                    operation.save()
                    
                    
                    
                else:
                    print("solde insufisant")

            elif type =="Versement":
                if compte.solde >= 0:
                    compte.solde +=  montant
                    compte.save()
                    operation.save()
                    
                    
                    
            return render(request, "base.html") 

        return render(request, "compte/add_operation.html")

    except:
        return HttpResponse("Compte inexistant")



def liste(request):
    clients = Client.objects.all()
    operations = Operation.objects.all()
    comptes = Compte.objects.all()

    return render(request, 'compte/liste.html', {"clients": clients, "operations": operations, "comptes": comptes})

def index(request):
    return render(request, "base.html")