from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt

import time

@csrf_exempt
def index(request, *args, **kwargs):
  print('request: ', request.method)
  if request.method == 'POST':
    print('headers: ', request.headers)
    print('body:    ', request.body)

    time.sleep(5)
    response = {}
    response['msg'] = 'hello world'
  return JsonResponse(response)