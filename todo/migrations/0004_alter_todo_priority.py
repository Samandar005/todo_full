# Generated by Django 5.1.5 on 2025-02-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(blank=True, choices=[('l', 'Low'), ('m', 'Medium'), ('h', 'High')], max_length=1),
        ),
    ]
