from django.shortcuts import render
from django.http import HttpResponse
from .models import ComputeInstance
from django.template import loader
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    instances = ComputeInstance.objects.order_by('-name')[:10]
    template = loader.get_template('instances/index.html')
    context = {'instances': instances}
    return HttpResponse(template.render(context, request))


@login_required
def detail(request, instanceId):
    return HttpResponse('Instance property: %s' % instanceId)