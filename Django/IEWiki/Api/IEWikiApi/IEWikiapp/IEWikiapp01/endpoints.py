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