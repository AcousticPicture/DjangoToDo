from django import forms
from .models import Category

class TaskForm(forms.Form):
    all_categories = Category.objects.all()
    choices = []
    for cat in all_categories:
        choices.append((cat.id, cat.name))

    content = forms.CharField(label='Inhalt', max_length=2000)
    input_formats = ['%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y'] 
    due_date = forms.DateField(input_formats=input_formats)
    important = forms.BooleanField()
    category_id = forms.ChoiceField(choices=choices)

class SortForm(forms.Form):
    choices = [
        (1, "Unsortiert"),
        (2, "Datum"),
        (3, "Erledigt"),
        (4, "Kategorie"),      
    ]

    all_categories = Category.objects.all()
    catChoices = []
    catChoices.append((len(all_categories)+1, "Keine Kategorie"))
    for cat in all_categories:
        catChoices.append((cat.id, cat.name))

    sortieren = forms.ChoiceField(choices=choices)
    filtern = forms.ChoiceField(choices=catChoices)

class CategoryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=150)
