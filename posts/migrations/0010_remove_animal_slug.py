# Generated by Django 2.2.7 on 2019-11-23 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_animal_shorttext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='slug',
        ),
    ]
