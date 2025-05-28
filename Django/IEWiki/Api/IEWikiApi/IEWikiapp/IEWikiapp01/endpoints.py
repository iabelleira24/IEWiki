import json

from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from .models import Jugador, Equipo, User


@csrf_exempt
def juego_1(request, precio):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)


    return JsonResponse({}, status=200)

@csrf_exempt
def juego_2(request, id, precio):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)


    return JsonResponse({"nombre": "gta VI","id": id, "precio":precio}, status=200)

@csrf_exempt
def juego_3(request, precio):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)


    return JsonResponse({"nombre": "gta VI","precio": precio}, status=200)

def juego_4(request, id):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)


    return JsonResponse({"nombre": "gta VI","id": id}, status=200)

def pregunta_1 (request):
    if request.method == "GET":
        equipo = request.GET.get('equipo','Raimon')
        print(f"Es un buen equipo el {equipo}!")
        return JsonResponse({'mensaje':f'Es un buen equipo el {equipo}!'})

def pregunta_2 (request, personaje):
    if request.method == "GET":
        equipo = request.GET.get('equipo','Raimon')
        print(f"Es un buen equipo el {equipo}!")
        return JsonResponse({'mensaje':f'Es un buen equipo el {equipo}!', "personaje": personaje}, status = 200)


def pregunta_3 (request):
    if request.method == "GET":
        equipo = request.GET.get('equipo')
        personaje = request.GET.get('personaje')

        if equipo and personaje:
            print(f"Equipo: {equipo}, Personaje: {personaje}")
            mensaje = f"{personaje} juega en el equipo {equipo}."
        elif equipo and not personaje:
            print(f"Solo se recibió el equipo: {equipo}")
            mensaje = f"El equipo proporcionado es {equipo}."
        elif personaje and not equipo:
            print(f"Solo se recibió el jugador: {personaje}")
            mensaje = f"El personaje proporcionado es {personaje}."
        else:
            print("No se recibió ni equipo ni personaje.")
            mensaje = "No se proporcionaron parametros."

        return JsonResponse({'mensaje': mensaje})


@csrf_exempt
def jugador(request, id):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

    try:
        j = Jugador.objects.get(id=id)
    except Jugador.DoesNotExist:
        return JsonResponse({"error": "Jugador not found."}, status=404)

    return JsonResponse({"id": j.id,"nombreJ":j.nombreJ, "posicionJ":j.posicionJ, "supertecnicaJ":j.supertecnicaJ, "equipoJ":j.equipoJ.nombreE, "imagenJ":j.imagenJ}, status=200)



@csrf_exempt
def jugadores(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

    jugadores = Jugador.objects.all()
    data = [{"id": jugador.id,
             "nombreJ":jugador.nombreJ,
             "posicionJ":jugador.posicionJ,
             "supertecnicaJ":jugador.supertecnicaJ,
             "equipoJ":jugador.equipoJ.nombreE
             } for jugador in jugadores]

    return JsonResponse({"jugadores": data}, status=200)





@csrf_exempt
def equipos(request):
    if request.method != "GET":
        return JsonResponse({"error": "Método HTTP no soportado"}, status=405)

    search = request.GET.get('search', '')

    if search:
        equipos = Equipo.objects.filter(
            Q(nombreE__icontains=search) | Q(entrenador__icontains=search)
        )
    else:
        equipos = Equipo.objects.all()

    data = [{
        'id': e.id,
        'nombreE': e.nombreE,
        'entrenador': e.entrenador,
        'imagen':e.imagen
    } for e in equipos]

    return JsonResponse({"equipos": data}, status=200)

@csrf_exempt
def jugadores_por_equipo(request, equipo_id):
    if request.method != "GET":
        return JsonResponse({"error": "Método HTTP no soportado"}, status=405)

    jugadores = Jugador.objects.filter(equipoJ__id=equipo_id)
    data = []

    for jugador in jugadores:
        imagen_url = jugador.imagenJ

        data.append({
            "id": jugador.id,
            "nombreJ": jugador.nombreJ,
            "posicionJ": jugador.posicionJ,
            "imagenJ": imagen_url
        })

    return JsonResponse({"jugadores": data}, status=200)



@csrf_exempt
def vecinos (request):
    if request.method != "POST":
        return JsonResponse({"error": "Método HTTP no soportado"}, status=405)

    json_data = json.loads(request.body)
    name = json_data.get('name')
    surname = json_data.get('surname')
    job = json_data.get('job')
    edad = json_data.get('edad')

    print(f"Nombre del nuevo vecino: {name} Apellido:  {surname} Trabaja de:  {job}  Dentro de 10 años tendrá:  {10 + edad}  años")
    return JsonResponse({})




@csrf_exempt
def presidentes (request):
    if request.method != "POST":
        return JsonResponse({"error": "Método HTTP no soportado"}, status=405)

    json_data = json.loads(request.body)
    nombre = json_data['nombre']
    apellidos = json_data['apellidos']
    agendaPolitica = json_data['agendaPolitica']
    objetivo = agendaPolitica.get('objetivo', 'No especificado')
    fechaNacimiento = json_data['fechaNacimiento']




    print (f"{nombre} {apellidos} su objetivo político es {objetivo}  . Ahora tiene {- int(fechaNacimiento [6] + fechaNacimiento [7] + fechaNacimiento [8] + fechaNacimiento [9])}")
    return JsonResponse({})



@csrf_exempt
def superheroes(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método HTTP no soportado"}, status=405)

    json_data = json.loads(request.body)

    nombre = json_data.get("nombre")
    color_favorito = json_data.get("color_favorito")
    dispositivo = json_data.get("dispositivo")
    formas = json_data.get("formas", [])

    print(f"El nuevo superheroe es {nombre}")
    print(f"Su color favoritos es {color_favorito} y su dispositivo es {dispositivo} ")
    print(f"Tiene estas formas:")

    for forma in formas:
        print(forma.get("nombre"))

    return JsonResponse({})



@csrf_exempt
def user(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método HTTP no soportado"}, status=405)

    json_data = json.loads(request.body)
    username = json_data.get("username")
    name = json_data.get("name")
    surname = json_data.get("surname")
    password = json_data.get("password")

    User.objects.create(username = username, name = name, surname = surname, password = password)


    return JsonResponse({"mensaje":"Se ha creado el usuario correctamente"}, status= 201)


@csrf_exempt
def sessions(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método HTTP no soportado"}, status=405)

    json_data = json.loads(request.body)
    username = json_data.get("username")
    password = json_data.get("password")

    try:
        user = User.objects.get(username =username)

        if password == user.password:
            print("La contraseña de " + user.username + "en BBDD es: " + user.password)
            return JsonResponse({"mensaje": "Usuario y contraseña correctas"}, status=200)

        return JsonResponse({"error": "password incorrecta."}, status=401)

    except User.DoesNotExist:
        return JsonResponse({"error": "User not found."}, status=404)




