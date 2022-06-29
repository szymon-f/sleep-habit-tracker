from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Asleep, Awake
from .forms import AddNewSleepEntry, AddNewAwakeEntry

# Create your views here.

def asleep(request):
    records = [x for x in Asleep.objects.all()]
    return render(request, 'asleep.html', {'records': records})

def awake(request):
    records = [x for x in Awake.objects.all()]
    return render(request, 'awake.html', {'records': records})

def dip(request):
    return HttpResponse("dip view")

def add(request):
    if request.method == "GET":
        form = AddNewSleepEntry()
        return render(request, 'add.html', {'form': form})
    elif request.method == "POST":
        form = AddNewSleepEntry(request.POST)
        if form.is_valid():
            receivedData = form.cleaned_data
            newEntry = Awake(note=receivedData['note'])
            newEntry.save()
        return HttpResponseRedirect('/habits/add')   #HttpResponse("<h1>Data received</h1><hr><a href=''>Go back</a>")
        