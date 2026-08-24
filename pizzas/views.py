from django.shortcuts import render

from .models import Pizza

def index(request):
    return render(request, 'pizzas/index.html')


# noinspection unresolved-references
def pizzas(request):
    them_pizzas = Pizza.objects.all()
    context = {'pizzas': them_pizzas}

    return render(request, 'pizzas/pizzas.html', context)

