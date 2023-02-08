# origen1 = "WA"
# dest1 = "TX;UT;VT;VA;WA;WV;WI;WY"
# ori2 = "KS"
# dest2 = "MN;MS;MI;MT"import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.db.models import Q
from .models import doftDB, routingDB, usersDB
import requests


def index(request):
    return HttpResponse("Aqui quedara el dashbard de FE-Routing")

def createProject(request):
    RUN_TOKEN = "t15qmr337RKO"
    api_key= "tGyD2-ahDS4Q"
    r = requests.get('https://www.parsehub.com/api/v2/runs/'+RUN_TOKEN+'/data?api_key='+api_key)
    return HttpResponse(r.text)


def getAllProjects(request):
    PROJECT_TOKEN = "tEWFZhVQXvnG"
    params = {
    "api_key": "tGyD2-ahDS4Q",
    "offset": "0",
    "include_options": "1"
    }
    r = requests.get('https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}', params=params)
    print(r.text)
    return HttpResponse(r.text)


def runProject(request):
    params = {
        "api_key": "tGyD2-ahDS4Q",
        "start_url": "http://www.example.com",
        "start_template": "main_template",
        "start_value_override": "{\"query\": \"San Francisco\"}",
        "send_email": "1"
        }
    r = requests.post("https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/run", data=params)

    return HttpResponse(r.text)


def ListAllProjects(request):
    params = {
        "api_key": "tGyD2-ahDS4Q",
        "offset": "0",
        "limit": "20",
        "include_options": "1"
    }   
    r = requests.get('https://www.parsehub.com/api/v2/projects', params=params)
    return HttpResponse(r.text)


def getARun(request):
    params = {
        "api_key": "tGyD2-ahDS4Q"
    }
    r = requests.get('https://www.parsehub.com/api/v2/runs/{RUN_TOKEN}', params=params)
    return HttpResponse(r.text)


def getDataForRun(request):
    params = {
        "api_key": "tGyD2-ahDS4Q",
        "format": "csv"
    }
    r = requests.get('https://www.parsehub.com/api/v2/runs/{RUN_TOKEN}/data', params=params)
    return HttpResponse(r.text)


def cancelRun(request):
    params = {
        "api_key": "tGyD2-ahDS4Q"
    }
    r = requests.post("https://www.parsehub.com/api/v2/runs/{RUN_TOKEN}/cancel", data=params)
    return HttpResponse(r.text)


def deleteRun(request):
    params = {
        "api_key": "tGyD2-ahDS4Q"
    }
    r = requests.delete('https://www.parsehub.com/api/v2/runs/{RUN_TOKEN}', params=params)
    return HttpResponse(r.text)


def GetLastReadyData(request):
    RUN_TOKEN = "t15qmr337RKO"
    api_key= "tGyD2-ahDS4Q"
    r = requests.get('https://www.parsehub.com/api/v2/runs/'+RUN_TOKEN+'/data?api_key='+api_key)
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
                    data.save()
        return HttpResponse('Se guardaron '+ str(contador) +' filas en la base de datos.')
    except:
        return HttpResponseBadRequest("Error en el envio de los datos")


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
                        data.save()
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
            cargas.save()
            return HttpResponse("Se ha guardado en la base de datos")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['GET'], "Metodo invalido")


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
        dataJson = json.dumps(allLoadsData)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")


def newsUsers(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) #data es un diccionario
            user = usersDB(
                id = data["id"],
                firstName = data["firstName"],
                lastName = data["lastName"],
                email = data["email"],
                password = data["password"]
            )#creo un objeto de tipo userDB a base del diccionario que tenia
            user.save()
            return HttpResponse("Nuevo usuario creado con exito!")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['GET'], "Metodo invalido")

def getOneUser(request, paramx):
    if request.method == 'GET':
        user = usersDB.objects.filter( id = id ).first()
        if (not user):
            return HttpResponseBadRequest("No existe usuario con esa cedula")
        data = {
            "id": usersDB.id,
            "firstName": usersDB.firstName,
            "lastName": usersDB.lastName,
            "email": usersDB.email
        }
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")

def getUsersByNames(request, paramx):
    if request.method == 'GET':
        user = usersDB.objects.filter( Q( firstName = paramx ) | Q( lastName = paramx ) )
        if (not user):
            return HttpResponseBadRequest("No existen usuarios con esos filtros")
        allUserData = []
        for x in user:
            data = {
                "id": x.id,
                "firstName": x.firstName,
                "lastName": x.lastName,
                "email": x.email
                }
            allUserData.append(data)
        dataJson = json.dumps(allUserData)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")