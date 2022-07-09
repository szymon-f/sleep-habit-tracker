from django.shortcuts import redirect, render, HttpResponse
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
        return HttpResponse("account created")
        
    else:
        form = RegisterForm()
        return render(request, 'sign-up.html', {'form': form})