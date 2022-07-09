from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Asleep, Awake, Dip, DreamNote
from .forms import AddNewSleepEntry, AddNewAwakeEntry, NewNote, AddNewDreamNote


def asleep(request):
    records = [x for x in Asleep.objects.all()][::-1]
    return render(request, 'asleep.html', {'records': records})

def awake(request):
    records = [x for x in Awake.objects.all()][::-1]
    return render(request, 'awake.html', {'records': records})

def dip(request):
    records = [x for x in Dip.objects.all()][::-1]
    return render(request, 'dip.html', {'records': records})

def dreamNotes(request):
    records = [x for x in DreamNote.objects.all()][::-1]
    return render(request, 'dream-notes.html', {'records': records})

def add(request):
    if request.method == "GET":
        form_normal = NewNote() #AddNewSleepEntry()
        form_dream = AddNewDreamNote()
        return render(request, 'add.html', {'form_normal': form_normal, 'form_dream': form_dream})
    elif request.method == "POST":
        if 'dream_note' in request.POST:
            form = AddNewDreamNote(request.POST)
            if form.is_valid():
                receivedData = form.cleaned_data
                newEntry = DreamNote(note=receivedData["note"])
                newEntry.save()
        else:
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
        