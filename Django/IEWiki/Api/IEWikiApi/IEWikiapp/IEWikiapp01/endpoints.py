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