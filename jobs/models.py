from django.db import models

#models to manage data to send to many types of databases
#all phots uploaded will be uplaoded to a central media folder i create
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
