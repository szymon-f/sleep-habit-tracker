from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Asleep, Awake, Dip, DreamNote
from .forms import AddNewSleepEntry, AddNewAwakeEntry, NewNote

# Create your views here.

def asleep(request):
    records = [x for x in Asleep.objects.all()]
    return render(request, 'asleep.html', {'records': records})

def awake(request):
    records = [x for x in Awake.objects.all()]
    return render(request, 'awake.html', {'records': records})

def dip(request):
    records = [x for x in Dip.objects.all()]
    return render(request, 'dip.html', {'records': records})

def dreamNotes(request):
    records = [x for x in DreamNote.objects.all()]
    return render(request, 'dream-notes.html', {'records': records})

def add(request):
    if request.method == "GET":
        form = NewNote() #AddNewSleepEntry()
        return render(request, 'add.html', {'form': form})
    elif request.method == "POST":
        form = NewNote(request.POST)
        if form.is_valid():
            receivedData = form.cleaned_data
            type = receivedData['type_of_note']
            match type:
                case 'dip':
                    newEntry = Dip(note=receivedData['note'])
                    newEntry.save()
                case 'awake':
                    newEntry = Awake(note=receivedData['note'])
                    newEntry.save()
                case 'asleep':
                    newEntry = Asleep(note=receivedData['note'])
                    newEntry.save()
        return HttpResponseRedirect('/habits/add')   
        