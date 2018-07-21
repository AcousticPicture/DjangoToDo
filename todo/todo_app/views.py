from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from .models import Entry
from .models import Category
from .forms import TaskForm
from .forms import FilterForm
from .forms import CategoryForm

# Create your views here.

def index(request):
    if "filter" in request.GET:
        filter = request.GET["filter"]
    else:
        filter = False

    form = FilterForm(request.GET)

    if filter is "2":
        all_todos = Entry.objects.order_by('due_date').all
    elif filter is "3":
        all_todos = Entry.objects.order_by('done').all
    elif filter is "4":
        all_todos = Entry.objects.order_by('category_id').all
    else:
        all_todos = Entry.objects.all

    template = loader.get_template('todo_app/index.html')
    context = { 'all_todos': all_todos, 'form': form}

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

def finish_task(request, id):
    if(request.method == 'POST'):
        task = Entry.objects.get(id=id)
        if task:
            task.done = True
            task.save()
    
    return redirect('index')

def new_category(request):
    if(request.method == 'POST'):
        form = CategoryForm(request.POST)
        form.is_valid()
        clean = form.cleaned_data
        cat = Category(name=clean['name'])
        cat.save()

        return redirect('index')
    else:
        template = loader.get_template('todo_app/category_form.html')
        form = CategoryForm()
        categories = Category.objects.all()
        print(categories)
        context = { 'form': form, 'category': categories}
        return HttpResponse(template.render(context, request))