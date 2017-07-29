#!-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from statistics.models import Data
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_protect
# Create your views here.


def index(request):
    """
    Shows index page of application
    :param request:
    :return: rendered html with list of possible regions inside
    """
    groups_queryset = Data.objects.values('region').distinct()
    group_list = []
    for item in groups_queryset:
        group_list.append(item['region'])
    return render_to_response('index.html', {'groups': group_list})


@csrf_protect
def answer(request):
    """
    Takes region from answer of js and filter DB, returns json with filtered data
    :param request:
    :return: HttpResponse with json inside
    """
    if request.method == "POST":
        region = request.POST.get('region')
        filtered_obj_by_region = Data.objects.filter(region=region).values('country', 'value')
        return HttpResponse(
            json.dumps(list(filtered_obj_by_region)),
            content_type="application/json"
        )