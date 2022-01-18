
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json

@csrf_exempt
def tg_web_hook(request):
    data = json.loads(request.body.decode('utf-8'))
    return JsonResponse(data)
