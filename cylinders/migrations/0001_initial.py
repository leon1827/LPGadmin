# Generated by Django 2.2 on 2020-02-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gp_code', models.CharField(default='000000', max_length=32)),
                ('zn_code', models.CharField(default='000000', max_length=32)),
                ('factory', models.CharField(default='百纳', max_length=32)),
                ('sc_date', models.CharField(default='201901', max_length=32)),
                ('jc_date', models.CharField(default='201901', max_length=32)),
                ('weight', models.CharField(default='16kg', max_length=32)),
                ('checka', models.CharField(default='杜扬', max_length=32)),
                ('fill_t', models.CharField(max_length=32)),
                ('process', models.CharField(default='正常', max_length=32)),
                ('checkb', models.CharField(default='张伟伟', max_length=32)),
                ('fillweight', models.CharField(default='29.5kg', max_length=32)),
                ('checkc', models.CharField(default='王光春', max_length=32)),
                ('remark', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jf_code', models.CharField(default='000000', max_length=32)),
                ('gp_code', models.CharField(default='000000', max_length=32)),
                ('zn_code', models.CharField(default='000000', max_length=32)),
                ('sc_date', models.CharField(default='201901', max_length=32)),
                ('jc_date', models.CharField(default='201901', max_length=32)),
                ('manufacturer', models.CharField(default='宣城百纳', max_length=100)),
                ('specification', models.CharField(default='YSP35.5', max_length=32)),
                ('company', models.CharField(default='青山液化气站', max_length=100)),
                ('xj_date', models.CharField(default='000000', max_length=32)),
                ('bf_date', models.CharField(default='000000', max_length=32)),
                ('remark', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(default='20190101', max_length=32)),
                ('gp_code', models.CharField(default='000000', max_length=32)),
                ('client', models.CharField(max_length=64)),
                ('tel', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=64)),
                ('remark', models.TextField(null=True)),
            ],
        ),
    ]