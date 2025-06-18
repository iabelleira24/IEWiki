import json
import secrets
import token
from urllib import request

from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.http import JsonResponse
from django.template.defaulttags import now
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime
from .models import Jugador, Equipo, User, Like, Videojuego, Supertecnica


@csrf_exempt
def juego_1(request, precio):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
    # 405 Method Not Allowed: Método HTTP no soportado para esta ruta

    return JsonResponse({}, status=200)
    # 200 OK: Petición exitosa

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
        # 404 Not Found: Recurso no encontrado
    token = request.headers.get('token')
    favorito = False

    if token:
        try:
            user = User.objects.get(tokenSessions=token)
            favorito = Like.objects.filter(user=user, jugador=j).exists()
        except User.DoesNotExist:
            pass  # Token inválido, dejamos favorito en False

    return JsonResponse({
        "id": j.id,
        "nombreJ": j.nombreJ,
        "posicionJ": j.posicionJ,
        "supertecnicaJ": j.supertecnicaJ,
        "equipoJ": j.equipoJ.nombreE,
        "imagenJ": j.imagenJ,
        "favorito": favorito
    }, status=200)


@csrf_exempt
def jugadores(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

    jugadores = Jugador.objects.all()
    data = [{"id": jugador.id,
             "nombreJ":jugador.nombreJ,
             "imagenJ": jugador.imagenJ
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

    token = request.headers.get('token')
    if not token:
        return JsonResponse({"error": "Token no encontrado"}, status=401)
        # 401 Unauthorized: Falta token para autorización

    try:
        user = User.objects.get(tokenSessions=token)
    except User.DoesNotExist:
        return JsonResponse({"error": "Token inválido"}, status=401)
        # 401 Unauthorized: Token inválido
    data = json.loads(request.body)
    jugador_id = data.get("jugadorId")
    jugador = Jugador.objects.get(id=jugador_id)
    like = request.GET.get('like', '')

    jugadores = Jugador.objects.filter(equipoJ__id=equipo_id)
    like = Like.objects.filter(user=user, jugador=jugador).first()
    if not like:
        imagen_url = jugador.imagenJ

        data = [{
            "id": jugador.id,
            "nombreJ": jugador.nombreJ,
            "posicionJ": jugador.posicionJ,
            "imagenJ": imagen_url
        } for jugador in jugadores]

        return JsonResponse({"jugadores": data}, status=200)
    favoritos = Like.objects.filter(user=user).select_related('jugador')
    data = [{
        "id": fav.jugador.id,
        "nombreJ": fav.jugador.nombreJ,
        "posicionJ": fav.jugador.posicionJ,
        "imagenJ": fav.jugador.imagenJ
    } for fav in favoritos]

    return JsonResponse({"favoritos": data}, status=200)



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
def presidentes(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método HTTP no soportado"}, status=405)

    json_data = json.loads(request.body)
    nombre = json_data['nombre']
    apellidos = json_data['apellidos']
    agendaPolitica = json_data['agendaPolitica']
    objetivo = agendaPolitica.get('objetivo', 'No especificado')
    fechaNacimiento = json_data['fechaNacimiento']  # formato: "YYYY-MM-DD"

    año_nacimiento = int(fechaNacimiento.split("-")[0])
    año_actual = datetime.now().year
    edad = año_actual - año_nacimiento

    print(f"{nombre} {apellidos} su objetivo político es {objetivo}. Nació en {año_nacimiento} y tiene {edad} años.")
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
    password = json_data.get("password")

    User.objects.create(username = username, password = password)


    return JsonResponse({"mensaje":"Se ha creado el usuario correctamente"}, status= 201)
    # 201 Created: Recurso creado exitosamente



@csrf_exempt
def sessions(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método HTTP no soportado"}, status=405)

    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
    except:
        return JsonResponse({"error": "Solicitud inválida"}, status=400)
        # 400 Bad Request: Solicitud inválida o mal formada

    user = User.objects.filter(username=username).first()
    if user is None:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)

    if user.password != password:
        return JsonResponse({"error": "Contraseña incorrecta"}, status=403)
        # 403 Forbidden: Acceso denegado, contraseña incorrecta

    token = secrets.token_hex(32)
    user.tokenSessions = token
    user.save()

    return JsonResponse({"token": token}, status=201)


@csrf_exempt
def like(request):
    if request.method != "PUT":
        return JsonResponse({"error": "Método HTTP no soportado"}, status=405)

    token = request.headers.get('token')
    if not token:
        return JsonResponse({"error": "Token no encontrado"}, status=401)
        # 401 Unauthorized: Falta token para autorización

    try:
        user = User.objects.get(tokenSessions=token)
    except User.DoesNotExist:
        return JsonResponse({"error": "Token inválido"}, status=401)
        # 401 Unauthorized: Token inválido

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Formato JSON inválido"}, status=400)

    jugador_id = data.get("jugadorId")
    if not jugador_id:
        return JsonResponse({"error": "ID del jugador no proporcionado"}, status=400)

    try:
        jugador = Jugador.objects.get(id=jugador_id)
    except Jugador.DoesNotExist:
        return JsonResponse({"error": "Jugador no encontrado"}, status=404)

    like_obj = Like.objects.filter(user=user, jugador=jugador).first()

    if like_obj:
        like_obj.delete()
        return JsonResponse({
            "mensaje": f"{jugador.nombreJ} eliminado de favoritos",
            "favorito": False
        }, status=200)
    else:
        Like.objects.create(user=user, jugador=jugador)
        return JsonResponse({
            "mensaje": f"{jugador.nombreJ} añadido a favoritos",
            "favorito": True
        }, status=200)




@csrf_exempt
def favoritos(request):
    if request.method != "GET":
        return JsonResponse({"error": "Método HTTP no soportado"}, status=405)

    token = request.headers.get('token')
    if not token:
        return JsonResponse({"error": "Token no encontrado"}, status=401)

    try:
        user = User.objects.get(tokenSessions=token)
    except User.DoesNotExist:
        return JsonResponse({"error": "Token inválido"}, status=401)

    favoritos = Like.objects.filter(user=user).select_related('jugador')
    data = [{
        "id": fav.jugador.id,
        "nombreJ": fav.jugador.nombreJ,
        "posicionJ": fav.jugador.posicionJ,
        "imagenJ": fav.jugador.imagenJ
    } for fav in favoritos]

    return JsonResponse({"favoritos": data}, status=200)


@csrf_exempt
def filtrados(request, equipo_id):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

    posicion = request.GET.get('posicion')
    if not posicion:
        return JsonResponse({"error": "Falta el parámetro 'posicion'"}, status=400)

    jugadores = Jugador.objects.filter(equipoJ__id=equipo_id, posicionJ=posicion)

    data = [{
        "id": jugador.id,
        "nombre": jugador.nombreJ,
        "posicion": jugador.posicionJ
    } for jugador in jugadores]

    return JsonResponse({"jugadores_filtrados": data}, status=200)


@csrf_exempt
def crear_videojuego(request):
    if request.method != "POST":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

    data = json.loads(request.body)
    nombre = data.get("nombre")
    jugador_id = data.get("jugador_id")
    equipo_id = data.get("equipo_id")
    plataforma = data.get("plataforma")

    try:
        jugador = Jugador.objects.get(id=jugador_id)
        equipo = Equipo.objects.get(id=equipo_id)
    except (Jugador.DoesNotExist, Equipo.DoesNotExist):
        return JsonResponse({"error": "Jugador o equipo no encontrado"}, status=404)

    Videojuego.objects.create(
        nombreVideojuego=nombre,
        jugador=jugador,
        equipo=equipo,
        plataforma=plataforma
    )

    return JsonResponse({"mensaje": "Videojuego creado correctamente"}, status=201)


@csrf_exempt
def actualizar_supertecnica(request, id):
    if request.method != "PUT":
        return JsonResponse({"error": "Método no soportado"}, status=405)

    token = request.headers.get("token")
    if not token:
        return JsonResponse({"error": "Token no proporcionado"}, status=401)

    try:
        user = User.objects.get(tokenSessions=token)
    except User.DoesNotExist:
        return JsonResponse({"error": "Token inválido"}, status=401)

    data = json.loads(request.body)
    nueva_tec = data.get("supertecnica")

    try:
        jugador = Jugador.objects.get(id=id)
    except Jugador.DoesNotExist:
        return JsonResponse({"error": "Jugador no encontrado"}, status=404)

    jugador.supertecnicaJ = nueva_tec
    jugador.save()

    return JsonResponse({"mensaje": "Supertecnica actualizada", "supertecnica": nueva_tec}, status=200)


@csrf_exempt
def videojuego_filtrado(request, nombreVideojuego, plataforma):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

    videojuegos = Videojuego.objects.filter(nombreVideojuego=nombreVideojuego, plataforma=plataforma)

    data = [{
        "nombreVideojuego": videojuego.nombreVideojuego,
        "plataforma": videojuego.plataforma
    } for videojuego in videojuegos]

    return JsonResponse({"videojuego_filtrado": data}, status=200)


@csrf_exempt
def supertecnica(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

    supertecnicas = Supertecnica.objects.all()
    data = [{
             "nombre": supertecnica.nombre,
             "descripcion": supertecnica.descripcion
            } for supertecnica in supertecnicas]

    return JsonResponse({"supertecnicas": data}, status=200)


@csrf_exempt
def user_username(request, username):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

    token = request.headers.get("token")

    data = json.loads(request.body)

    username = data.get("username")
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        return JsonResponse({"error": "User no encontrado"}, status=404)

    user = User.objects.get(tokenSessions=token)
    isLoggedIn = True
    if user is None:
        isLoggedIn = False
        return JsonResponse({"username": username, isLoggedIn : isLoggedIn}, status=200)

    data = [{
        "username": user.username,
        "isLoggedIn": isLoggedIn
    }]

    return JsonResponse({"user": data}, status=200)
