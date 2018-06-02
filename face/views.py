import datetime
import json

import requests

from django.shortcuts import render
from .models import Action, Person
from django.http import HttpResponse


def index(request):
    all_record = Action.objects.order_by('-time')
    return render(request, 'index.html', context={
        'records': all_record,
    })


def interaction(request, face_token):
    # 人脸比对
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    key = "3ei-LSMaC_8xJONBn3c6-14BZpIxfr9w"
    secret = "WPoOvgMNXiryEwSS_aOj0tbINJzlJVCY"
    data = {
        "api_key": key,
        "api_secret": secret,
        "faceset_token": "ebf222df9586a44829c5546698cec44b",
        "face_token": face_token,
        }

    while True:
        response = requests.post(http_url, data=data)
        response = json.loads(response.text)
        if not response.get('error_message'):
            break

    conf = response["results"][0]["confidence"]

    # 获取置信度
    e_5 = response["thresholds"]["1e-5"]
    e_4 = response["thresholds"]["1e-4"]

    # 对比结果置信度
    if conf > e_4:
        # 从 FaceSet 中搜索出的一个人脸标识 face_token
        token = response["results"][0]["face_token"]

        person = Person.objects.filter(face_token=token)[0]
        record = Action()
        record.name = person.name
        record.identity = person.identity
        record.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        record.save()
        return HttpResponse(True)
    else:
        return HttpResponse(False)

