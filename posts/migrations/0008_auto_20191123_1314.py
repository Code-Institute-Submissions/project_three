# Generated by Django 2.2.7 on 2019-11-23 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_animal_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='behaviour',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='size',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
