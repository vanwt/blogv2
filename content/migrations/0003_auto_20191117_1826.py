# Generated by Django 3.0b1 on 2019-11-17 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20191117_1824'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='whitelist',
            options={'verbose_name': '名单', 'verbose_name_plural': '名单'},
        ),
        migrations.AlterModelTable(
            name='whitelist',
            table='white_list',
        ),
    ]