# Generated by Django 2.2 on 2020-02-03 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cylinders', '0003_record_inputtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filling',
            name='jc_date',
            field=models.DateField(verbose_name='jc_date'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='sc_date',
            field=models.DateField(verbose_name='sc_date'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='bf_date',
            field=models.DateField(verbose_name='bf_date'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='jc_date',
            field=models.DateField(verbose_name='jc_date'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='sc_date',
            field=models.DateField(verbose_name='sc_date'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='xj_date',
            field=models.DateField(verbose_name='xj_date'),
        ),
    ]