from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.GenericIPAddressField(null=True, default=None)
    agentPort = models.IntegerField(null=True, default=None)
    natHidden = models.BooleanField(default=True)
    lastContact = models.DateTimeField(auto_now=False, blank=True, null=True, default=None)
    clientKey = models.CharField(max_length=50, null=False, default='')

    @classmethod
    def new(cls, name, clientKey):
        dev = cls(name=name, clientKey=clientKey)
        return dev


class Service(models.Model):
    name = models.CharField(max_length=50)
    port = models.IntegerField()


class DeviceServices(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    #set only if the service port is different from original service
    port = models.IntegerField(null=True)

