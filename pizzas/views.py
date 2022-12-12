from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizza_choices(request):
    pizza_choices = Pizza.objects.all

    context = {'all_pizza_choices':pizza_choices}
    return render(request, 'pizzas/pizza_choices.html', context)



def pizza(request, topic_id):
    p = Pizza.objects.get(id=topic_id)

    entries = Topping.objects.filter(pizza=p)
    
    context = {'pizza':p, 'entries':entries}

    return render(request, 'pizzas/pizza.html', context)