# cursos/views.py

from django.shortcuts import render
from .models import Depoimento
from .forms import DepoimentoForm

def home(request):
    depoimento_form = DepoimentoForm(request.POST or None)
    if request.method == 'POST' and depoimento_form.is_valid():
        depoimento_form.save()
    
    return render(request, 'home.html', {'depoimento_form': depoimento_form})



#def home(request):
#    return render(request, 'home.html')