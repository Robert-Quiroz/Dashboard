import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from .models import doftDB, routingDB
import requests


def pruebaapi(request):
    RUN_TOKEN = "t15qmr337RKO"
    api_key= "tGyD2-ahDS4Q"
    r = requests.get('https://www.parsehub.com/api/v2/runs/'+RUN_TOKEN+'/data?api_key='+api_key)
    #return HttpResponse(r.text)
    contador = 0
    try:
        predata = json.loads(r.text) #predata es un diccionario
        for x in predata:
            if x == "LoadInfo":
                for y in range(len(predata[x])):
                    contador+=1
                    data = doftDB(
                        pickups = predata[x][y]["Pickup"],
                        origins = predata[x][y]["Orgin"],
                        states_orign = predata[x][y]["StateOrig"],
                        destinations = predata[x][y]["Destination"],
                        states_dest = predata[x][y]["StateDest"],
                        weights = predata[x][y]["Weight"],
                        distances = predata[x][y]["Distance"],
                        truck_types = predata[x][y]["TruckType"]
                    )
                    data.save() #guardo en la base de datos
        return HttpResponse('Se guardaron '+ str(contador) +' filas en la base de datos.')
    except:
        return HttpResponseBadRequest("Error en el envio de los datos")


def index(request):
    return HttpResponse("Aqui quedara el dashbard de FE-Routing")


def prueba(request):
    if request.method == 'GET':
        try:
            predata = json.loads(request.body) #predata es un diccionario
            for x in predata:
                if x == "LoadInfo":
                    for y in range(len(predata[x])):
                        print(predata[x][y]["Pickup"])
                        data = doftDB(
                            pickups = predata[x][y]["Pickup"],
                            origins = predata[x][y]["Orgin"],
                            states_orign = predata[x][y]["StateOrig"],
                            destinations = predata[x][y]["Destination"],
                            states_dest = predata[x][y]["StateDest"],
                            weights = predata[x][y]["Weight"],
                            distances = predata[x][y]["Distance"],
                            truck_types = predata[x][y]["TruckType"]
                        )
                        data.save() #guardo en la base de datos
            return HttpResponse(data)
        except:
            return HttpResponseBadRequest("Error en el envio de los datos")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")


def newsLoadsDoftDB(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) #data es un diccionario
            cargas = doftDB(
                pickups = data["Pickup"],
                origins = data["Orgin"],
                states_orign = data["StateOrig"],
                destinations = data["Destination"],
                states_dest = data["StateDest"],
                weights = data["Weight"],
                distances = data["Distance"],
                truck_types = data["TruckType"]
            )#creo un objeto de tipo doftDB a base del diccionario que tenia
            cargas.save()#guardo en la base de datos
            return HttpResponse("Se ha guardado en la base de datos")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")


def getLoadsDoftBD(request):
    if request.method == 'GET':
        cargas = doftDB.objects.all() #SELECT * FROM DOFTDB, esto es un queryset
        allLoadsData = [] #Creo una lista
        for x in cargas: #recorro la lista, creo un diccionario y lo lleno
            data = {
                "id": x.id,
                "Pickup": x.pickups,
                "Orgin": x.origins,
                "StateOrig": x.states_orign,
                "Destination": x.destinations,
                "StateDest": x.states_dest,
                "Weight": x.weights,
                "Distance": x.distances,
                "TruckType": x.truck_types
            } 
            allLoadsData.append(data) #añado a la lista
        datajason = json.dumps(allLoadsData)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = datajason
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Metodo invalido")

# PROJECT_TOKEN = "tEWFZhVQXvnG"
# projectToken = "tEWFZhVQXvnG"
# apiKey = "tGyD2-ahDS4Q"
# origen1 = "WA"
# dest1 = "TX;UT;VT;VA;WA;WV;WI;WY"
# ori2 = "KS"
# dest2 = "MN;MS;MI;MT"
# def createProject(request):
#     if fi:
#         sfgsdfs
#     else:
#         sdfsdf

# def getAllProjects(request):
#     if fi:
#         sfgsdfs
#     else:
#         sdfsdf

# def runProject(request):
#     if fi:
#         sfgsdfs
#     else:
#         sdfsdf

# def getDataForRunProject(request):
#     if fi:
#         sfgsdfs
#     else:
#         sdfsdf

# def cancelRun(request):
#     if fi:
#         sfgsdfs
#     else:
#         sdfsdf

# def deleteRun(request):
#     if fi:
#         sfgsdfs
#     else:
#         sd