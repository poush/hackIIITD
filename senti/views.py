# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    x = request.POST.get('text')
    print(x)
    return JsonResponse({'rate':'77.8'})
