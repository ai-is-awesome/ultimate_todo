# Generated by Django 2.2.7 on 2020-03-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0005_task_archive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]