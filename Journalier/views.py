from django.shortcuts import redirect, render, get_object_or_404
from .forms import Formtask
from .models import task 

def index (request): 
    form = Formtask(request.POST or None)
    if form.is_valid():
        form.save()
    list = task.objects.all()
    context ={
        'form': form, 
        'taches': list, 
    }
    return render(request, 'index.html', context) 

def update(request, my_id): 
    obj = get_object_or_404(task, id=my_id)
    form = Formtask(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form})

def delete(request, my_id):
    obj = get_object_or_404(task, id=my_id)
    obj.delete()
    return redirect('/')

