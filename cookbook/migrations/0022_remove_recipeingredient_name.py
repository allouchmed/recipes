# Generated by Django 3.0.2 on 2020-02-16 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0021_auto_20200216_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='name',
        ),
    ]
