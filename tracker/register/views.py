from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponseRedirect
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/register")
        
    else:
        form = RegisterForm()
        return render(request, 'sign-up.html', {'form': form})