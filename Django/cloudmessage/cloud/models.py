from django.db import models


class Message(models.Model):
    yourName = models.CharField(max_length=20)
    yourTelephone = models.CharField(max_length=20)
    message = models.CharField(max_length=200)
    otherName = models.CharField(max_length=20)
    otherTelephone = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

