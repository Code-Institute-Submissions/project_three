# Generated by Django 2.2.7 on 2019-12-30 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_auto_20191227_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='reptiletype',
            field=models.CharField(choices=[('X', 'Choose type of reptile'), ('C', 'Crocodile'), ('L', 'Lizard'), ('S', 'Snake'), ('T', 'Turtle')], default='X', max_length=7),
        ),
    ]
