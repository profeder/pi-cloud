from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Device
from django.template import loader
from django.contrib.auth.decorators import login_required
import random, string


@login_required
def index(request):
    devices = Device.objects.all()
    nPages =Device.objects.count()
    template = loader.get_template('index.html')
    context = {
        'devices': devices,
        'pages': nPages
    }
    return HttpResponse(template.render(context, request))

@login_required
def new(request):
    if request.method == 'POST':
        dev = Device.new(name=request.POST['name'], clientKey= request.POST['clientKey'])
        dev.save()
        context = {
            'messages': {
                'status': 'OK',
                'message': 'Devices sucessful insert'
            }
        }
        return redirect('/devices', context)
    template = loader.get_template('new.html')
    clientKey = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(50))
    context = {'clientKey': clientKey}
    return HttpResponse(template.render(context, request))