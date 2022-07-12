from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Asleep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asleep', null=True)
    date = models.DateTimeField(default=timezone.now()) 
    note = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.note

class Awake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='awake', null=True)
    date = models.DateTimeField(default=timezone.now()) 
    note = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.note

class Dip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dip', null=True)
    date = models.DateTimeField(default=timezone.now()) 
    note = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.note

class DreamNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dream_note', null=True)
    date = models.DateTimeField(default=timezone.now())
    note = models.CharField(max_length=2000)
    def __str__(self):
        return self.note
