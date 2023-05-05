# cursos/views.py

from django.shortcuts import render
from .models import Contato
from .forms import ContatoForm

def home(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContatoForm()
    
    return render(request, 'home.html', {'form': form})



#def home(request):
#    return render(request, 'home.html')