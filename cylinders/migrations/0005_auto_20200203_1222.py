# Generated by Django 2.2 on 2020-02-03 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cylinders', '0004_auto_20200203_1155'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Filling',
        ),
        migrations.DeleteModel(
            name='Gp',
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]
