from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Entry
from .models import Category

# Create your views here.

def index(request):
    all_todos = Entry.objects.all
    all_categories = Category.objects.all
    template = loader.get_template('todo_app/index.html')
    context = { 'all_todos': all_todos}
    return HttpResponse(template.render(context, request))

def newTask(request):
    if(request.method == 'POST'):
        text = request.POST['text']
        due_date = request.POST['due_date']
        done = request.POST['done']
        category = request.POST['category']
        newTask = Entry(text=text, due_date=due_date, done = done, category=category)
        newTask.save()
        return redirect()

def editTask(request, id):
    todo = Entry.objects.get(id=id)
    