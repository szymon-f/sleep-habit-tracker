from django.shortcuts import render
from django.http import HttpResponse
from .models import Asleep
from .forms import AddNewSleepEntry

# Create your views here.

def asleep(request):
    records = [x for x in Asleep.objects.all()]
    return render(request, 'asleep.html', {'records': records})

def awake(request):
    return HttpResponse("wake view")

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
            NewEntry = Asleep(note=receivedData['note'])
            NewEntry.save()
        return HttpResponse("<h1>Data received</h1><hr><a href=''>Go back</a>")