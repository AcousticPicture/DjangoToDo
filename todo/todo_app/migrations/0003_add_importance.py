# Generated by Django 2.0.7 on 2018-07-25 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_auto_20180709_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
