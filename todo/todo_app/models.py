from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

class Entry(models.Model):
    text = models.CharField(max_length=2000)
    due_date = models.DateTimeField()
    done = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
