from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.apps import apps
import socket
import datetime

def natTest(request, clientId, port):
    Device = apps.get_model('devices', 'Device')
    client = Device.objects.filter(clientKey=clientId)


    if not client:
        return HttpResponse(status=401)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((request.META['REMOTE_ADDR'], port))
        s.close()
        hidden = False
    except socket.error:
        hidden = True
    client.update(address=request.META['REMOTE_ADDR'], agentPort=port, lastContact=datetime.datetime.now(), natHidden=hidden)
    dataSerializzer = serializers.serialize('json', client)
    return JsonResponse(dataSerializzer, safe=False)