# Generated by Django 2.0.7 on 2018-07-09 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='category',
            new_name='category_id',
        ),
    ]