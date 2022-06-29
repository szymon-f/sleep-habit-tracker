from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
"""class Habit(models.Model):
    type = models.CharField(max_length=64)
    def __str__(self):
        return self.type

class Asleep(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    note = models.CharField(max_length=200, blank=True)
    asleep_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Awake(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    note = models.CharField(max_length=200, blank=True)
    awake_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Dip(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    note = models.CharField(max_length=200, blank=True)
    dip_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)"""

class Asleep(models.Model):
    date = models.DateTimeField(default=timezone.now()) #datetime.now()
    note = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.note

class Awake(models.Model):
    date = models.DateTimeField(default=timezone.now()) #datetime.now()
    note = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.note

class Dip(models.Model):
    date = models.DateTimeField(default=timezone.now()) #datetime.now()
    note = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.note

class DreamNote(models.Model):
    date = models.DateTimeField(default=timezone.now())
    note = models.CharField(max_length=2000)
    def __str__(self):
        return self.note
