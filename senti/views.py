# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from pick.test import check
from .models import User

@csrf_exempt
def index(request):
    x = json.loads(request.body).get('post')
    print(x)
    obj, created = User.objects.get_or_create(
        username=x.get('username'),
        defaults={'score': 0},
    )
    a, flag = check(x.get('cooked'), obj.score)
    obj.update(score=a)
    if flag:
        print('Send email')

    return 'success'
