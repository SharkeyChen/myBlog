from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import utc
import json
from blog import models
# Create your views here.

import datetime
import time


#重写Encoder
class DateEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, o)


def blog(request):
    return render(request, 'index.html')


@csrf_exempt #增加装饰器，跳过csrf中间件保护
def leaveMessage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        models.messageMail.objects.create(
            name=name,
            email=email,
            message=message,
            date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
        )
        return HttpResponse("yes")

@csrf_exempt #增加装饰器，跳过csrf中间件保护
def getMessageList(request):
    if request.method == "POST":
        DBlist = models.messageMail.objects.all().values_list()
        data = json.dumps(list(DBlist), cls=DateEncoder)
        return HttpResponse(data)

