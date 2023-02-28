# origen1 = "WA"
# dest1 = "TX;UT;VT;VA;WA;WV;WI;WY"
# ori2 = "KS"
# dest2 = "MN;MS;MI;MT"import json
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.db.models import Q
from .models import doftDB, routingDB, usersDB
import requests
from django.template import loader
from collections import Counter

def pie_chart(request):
    return render(request, 'pie_chart.html', )

def doughnut_chart(request):
    return render(request, 'doughnut_chart.html', )


def origin_destination_scatter(request):
    data = doftDB.objects.all()

    # Generar una lista de objetos para representar cada punto en la gráfica de dispersión
    scatter_data = []
    for item in data:
        scatter_data.append({'x': item.origins, 'y': item.destinations})
    # Pasar la lista de objetos como un objeto JSON
    scatter_data_json = json.dumps(scatter_data)
    print(scatter_data_json)

    return render(request, 'scatter_chart.html', {'scatter_data_json': scatter_data_json})


def origin_destination_chart(request):
    origins = doftDB.objects.order_by().values_list('origins', flat=True).distinct()
    destinations = doftDB.objects.order_by().values_list('destinations', flat=True).distinct()
    
    frequency = {}
    
    for origin in origins:
        for destination in destinations:
            count = doftDB.objects.filter(origins=origin, destinations=destination).count()
            if count > 0:
                frequency[(origin, destination)] = count
    
    the_labels = []
    the_data = []
    
    for origin, destination in sorted(frequency, key=frequency.get, reverse=True):
        the_labels.append(f"{origin} - {destination}")
        the_data.append(frequency[(origin, destination)])
    return render(request, "chartss.html", {'the_labels': the_labels, 'the_data': the_data})


def my_view(request):
    origins = doftDB.objects.order_by().values_list('origins', flat=True).distinct()
    destinations = doftDB.objects.order_by().values_list('destinations', flat=True).distinct()
    
    frequency = {}
    
    for origin in origins:
        for destination in destinations:
            count = doftDB.objects.filter(origins=origin, destinations=destination).count()
            if count > 0:
                frequency[(origin, destination)] = count
    
    the_labels = []
    the_data = []
    
    for origin, destination in sorted(frequency, key=frequency.get, reverse=True):
        the_labels.append(f"{origin} - {destination}")
        the_data.append(frequency[(origin, destination)])

    pickups_data = doftDB.objects.all().values_list('pickups', flat=True)
    pickups_counts = dict(Counter(pickups_data))
    pickups_list = list(pickups_counts.keys())
    pickups_counts_list = list(pickups_counts.values())

    states_orign_data = doftDB.objects.values_list('states_orign', flat=True)
    states_orign_counts = dict(Counter(states_orign_data))
    states_orign_list = list(states_orign_counts.keys())
    states_orign_counts_list = list(states_orign_counts.values())

    origins_data = doftDB.objects.values_list('origins', flat=True)
    origins_counts = dict(Counter(origins_data))
    origins_list = list(origins_counts.keys())
    origins_counts_list = list(origins_counts.values())

    states_dest_data = doftDB.objects.values_list('states_dest', flat=True)
    states_dest_counts = dict(Counter(states_dest_data))
    states_dest_list = list(states_dest_counts.keys())
    states_dest_counts_list = list(states_dest_counts.values())

    destinations_data = doftDB.objects.values_list('destinations', flat=True)
    destinations_counts = dict(Counter(destinations_data))
    destinations_list = list(destinations_counts.keys())
    destinations_counts_list = list(destinations_counts.values())

    distances = doftDB.objects.values_list('distances', flat=True)
    distances_data = []
    distances_counts = dict(Counter(distances))
    for key, value in distances_counts.items():
        distance_num = float(key.split()[0])
        distances_data.append({'label': key, 'value': value, 'distance_num': distance_num})
    
    truck_types_data = doftDB.objects.values_list('truck_types', flat=True)
    truck_types_counts = dict(Counter(truck_types_data))
    truck_types_list = list(truck_types_counts.keys())
    truck_types_counts_list = list(truck_types_counts.values())
    
    weights_list = doftDB.objects.values_list('weights', flat=True)
    weights_dict = {}
    for weight in weights_list:
        try:
            weight_num = float(weight.split()[0].rstrip('k'))
        except ValueError:  # handle non-numeric values
            weight_num = 0
        if weight_num not in weights_dict:
            weights_dict[weight_num] = 1
        else:
            weights_dict[weight_num] += 1
    weights_labels = list(weights_dict.keys())
    weights_data = list(weights_dict.values())

    return render(request, 'bar_chart.html', {'pickups_list': pickups_list, 'pickups_counts_list': pickups_counts_list, 'states_orign_list': states_orign_list, 'states_orign_counts_list': states_orign_counts_list,'origins_list': origins_list, 'origins_counts_list': origins_counts_list,'states_dest_list': states_dest_list, 'states_dest_counts_list': states_dest_counts_list,'destinations_list': destinations_list, 'destinations_counts_list': destinations_counts_list, 'distances_data': distances_data,'truck_types_list': truck_types_list, 'truck_types_counts_list': truck_types_counts_list,'weights_labels': weights_labels, 'weights_data': weights_data,'the_labels': the_labels, 'the_data': the_data,})

def load_data(request):
    la_data = doftDB.objects.all().values()
    template = loader.get_template('bar_chart.html')
    context = {'la_data': la_data,}
    return HttpResponse(template.render(context, request))


def tables(request):
    all_Loads = doftDB.objects.all().values()
    template = loader.get_template('tables.html')
    context = {'all_Loads': all_Loads,}
    return HttpResponse(template.render(context, request))


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def charts(request):
    all_Loads2 = doftDB.objects.all().values()
    template = loader.get_template('charts.html')
    context = {'all_Loads2': all_Loads2,}
    return HttpResponse(template.render(context, request))


def tables(request):
    all_Loads = doftDB.objects.all().values()
    template = loader.get_template('tables.html')
    context = {'all_Loads': all_Loads,}
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())


def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())


def forgotPassword(request):
    template = loader.get_template('forgot-password.html')
    return HttpResponse(template.render())


def proyects(request):
    template = loader.get_template('buttons.html')
    return HttpResponse(template.render())


def data(request):
    template = loader.get_template('cards.html')
    return HttpResponse(template.render())


def getAProject(request):
    PROJECT_TOKEN = "tEWFZhVQXvnG"
    params = {
    "api_key": "tGyD2-ahDS4Q",
    "offset": "0",
    "include_options": "1"
    }
    r = requests.get('https://www.parsehub.com/api/v2/projects/'+PROJECT_TOKEN, params=params)
    #print(r.text)
    return HttpResponse(r.text)


def runProject(request):
    PROJECT_TOKEN = "tEWFZhVQXvnG"
    params = {
        "api_key": "tGyD2-ahDS4Q",
        "start_url": "https://loadboard.doft.com/login",
        "start_template": "main_template",
        #"start_value_override": "{\"query\": \"San Francisco\"}",
        #"send_email": "1"
        }
    r = requests.post("https://www.parsehub.com/api/v2/projects/"+PROJECT_TOKEN+"/run", data=params)

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
    RUN_TOKEN = "t15qmr337RKO"
    params = {
        "api_key": "tGyD2-ahDS4Q"
    }
    r = requests.get('https://www.parsehub.com/api/v2/runs/'+RUN_TOKEN, params=params)
    return HttpResponse(r.text)


def getDataForRun(request):
    RUN_TOKEN = "t15qmr337RKO"
    params = {
        "api_key": "tGyD2-ahDS4Q",
        "format": "json"
    }
    r = requests.get('https://www.parsehub.com/api/v2/runs/'+RUN_TOKEN+'/data', params=params)
    return HttpResponse(r.text)


def cancelRun(request):
    RUN_TOKEN = "t15qmr337RKO"
    params = {
        "api_key": "tGyD2-ahDS4Q"
    }
    r = requests.post("https://www.parsehub.com/api/v2/runs/"+RUN_TOKEN+"/cancel", data=params)
    return HttpResponse(r.text)


def deleteRun(request):
    RUN_TOKEN = "t15qmr337RKO"
    params = {
        "api_key": "tGyD2-ahDS4Q"
    }
    r = requests.delete('https://www.parsehub.com/api/v2/runs/'+RUN_TOKEN, params=params)
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
                truck_types = data["TruckType"],
            )#creo un objeto de tipo doftDB a base del diccionario que tenia
            cargas.save()
            return HttpResponse("Se ha guardado las cargas en la base de datos")
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
        data_json = json.dumps(allLoadsData)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = data_json
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Metodo invalido")


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
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")

def getOneUser(request, id):
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
        return HttpResponseNotAllowed(['GET'], "Metodo invalido")

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
        return HttpResponseNotAllowed(['GET'], "Metodo invalido")


def updateUsers(request, id):
    if request.method == 'PUT':
        try:
            user = usersDB.objects.filter( id = id ).first()
            if (not user):
                return HttpResponseBadRequest("No existe usuario con esa cedula")
            
            data = json.loads(request.body) #data es un diccionario
            user.firstName = data["firstName"],
            user.lastName = data["lastName"],
            user.email = data["email"],
            user.password = data["password"]
            user.save()
            return HttpResponse("Usuario ACTUALIZADO con exito!")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Metodo invalido")


def deleteUsers(request, id):
    if request.method == 'DELETE':
        try:
            user = usersDB.objects.filter( id = id ).first()
            if (not user):
                return HttpResponseBadRequest("No existe usuario con esa cedula")

            user.delete()
            return HttpResponse("Usuario ELIMINADO con exito!")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Metodo invalido")