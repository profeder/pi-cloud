from django.db import models


class ComputeInstance(models.Model):
    name = models.CharField(max_length=200)
    insert_date = models.DateTimeField()
    active = models.BooleanField()


class Credential(models.Model):
    username = models.CharField(max_length=50, default='root')
    computeInstance = models.ForeignKey(ComputeInstance, on_delete=models.CASCADE)
    private_key = models.BinaryField()
    password = models.CharField(max_length=100)
    begin_date = models.DateTimeField(auto_now_add=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

