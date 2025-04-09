import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def json_1(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)


    return JsonResponse({})


@csrf_exempt
def json_2(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)


    return JsonResponse({"nombre": "Iago"})
@csrf_exempt
def json_3(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)


    return JsonResponse({"Suerte": "Mucha", "nota": 10})

@csrf_exempt
def json_4(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)


    return JsonResponse([1, 2, 3], safe=False)

@csrf_exempt
def json_5(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)


    return JsonResponse(["a", "b", "c"], safe=False)

@csrf_exempt
def json_6(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)


    return JsonResponse([{"nombre": "Iago"}, {"nombre": "Christian"}], safe=False)


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