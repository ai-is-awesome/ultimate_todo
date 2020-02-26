# Generated by Django 2.2.7 on 2020-02-26 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
