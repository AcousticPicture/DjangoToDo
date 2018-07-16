from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from .models import Entry
from .models import Category
from .forms import TaskForm

# Create your views here.

def index(request):
    all_todos = Entry.objects.all
    all_categories = Category.objects.all
    template = loader.get_template('todo_app/index.html')
    context = { 'all_todos': all_todos}
    return HttpResponse(template.render(context, request))

def new_task(request):
    if(request.method == 'POST'):
        form = TaskForm(request.POST)
        form.is_valid()
        clean = form.cleaned_data
        cat = Category.objects.get(pk=clean['category_id'])
        task = Entry(text=clean['content'], due_date=clean['due_date'], done=False, category_id=cat)
        task.save()

        return redirect('index')
    else:
        template = loader.get_template('todo_app/task_form.html')
        form = TaskForm()
        context = { 'form': form}
        return HttpResponse(template.render(context, request))

def edit_task(request, id):
    task = Entry.objects.get(id=id)
    if(request.method == 'POST'):
        form = TaskForm(request.POST)
        form.is_valid()
        clean = form.cleaned_data
        cat = Category.objects.get(pk=clean['category_id'])

        task.text = clean['content']
        task.due_date = clean['due_date']
        task.category_id = cat
        task.save()

        return redirect('index')
    else:
        initial = {
            'content': task.text,
            'due_date': task.due_date,
            'category_id': task.category_id.id
        }
        template = loader.get_template('todo_app/task_form.html')
        form = TaskForm(initial=initial)
        context = { 'form': form}
        return HttpResponse(template.render(context, request))
    
def delete_task(request, id):
    if(request.method == 'POST'):
        task = Entry.objects.get(id=id)
        task.delete()
    
    return redirect('index')
        