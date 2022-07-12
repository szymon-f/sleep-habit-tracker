from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Asleep, Awake, Dip, DreamNote
from .forms import  NewNote, AddNewDreamNote


def asleep(request):
    return render(request, 'asleep.html', {})

def awake(request):
    return render(request, 'awake.html', {})

def dip(request):
    return render(request, 'dip.html', {})

def dreamNotes(request):
    return render(request, 'dream-notes.html', {})

def add(request):
    if request.method == "GET":
        form_normal = NewNote()
        form_dream = AddNewDreamNote()
        return render(request, 'add.html', {'form_normal': form_normal, 'form_dream': form_dream})
    elif request.method == "POST":
        if 'dream_note' in request.POST:
            form = AddNewDreamNote(request.POST)
            if form.is_valid():
                note = form.cleaned_data['note']
                newEntry = DreamNote(note=note)
                newEntry.save()
                request.user.dream_note.add(newEntry)
        else:
            form = NewNote(request.POST)
            if form.is_valid():
                note = form.cleaned_data['note']
                type = form.cleaned_data['type_of_note']
                match type:
                    case 'dip':
                        newEntry = Dip(note=note)
                        newEntry.save()
                        request.user.dip.add(newEntry)
                    case 'awake':
                        newEntry = Awake(note=note)
                        newEntry.save()
                        request.user.awake.add(newEntry)
                    case 'asleep':
                        newEntry = Asleep(note=note)
                        newEntry.save()
                        request.user.asleep.add(newEntry)
        return HttpResponseRedirect('/habits/add')   
        