# Generated by Django 3.0b1 on 2019-11-17 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
        ('note', '0002_auto_20191117_1816'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Note',
        ),
    ]
