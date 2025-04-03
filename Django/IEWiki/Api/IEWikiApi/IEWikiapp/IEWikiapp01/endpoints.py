import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def json_1(request):
    if request.method != "GET":
        return JsonResponse({"error": "HTTP method not supported"}, status=405)


    return JsonResponse({})