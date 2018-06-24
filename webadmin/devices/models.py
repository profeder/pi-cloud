from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=255)
    address = models.IPAddressField(null=True)
    agentPort = models.IntegerField(null=True)
    natHidden = models.BooleanField(null=True)
    lastContact = models.DateTimeField(auto_now=False, blank=True, null=True)

class Service(models.Model):
    name = models.CharField(max_length=50)
    port = models.IntegerField()

class DeviceServices(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    #set only if the service port is different from original service
    port = models.IntegerField(null=True)