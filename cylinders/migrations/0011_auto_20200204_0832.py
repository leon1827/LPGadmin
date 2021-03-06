# Generated by Django 2.2 on 2020-02-04 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cylinders', '0010_auto_20200204_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filling',
            name='checka',
            field=models.CharField(default='杜扬', max_length=32, verbose_name='充前检查员'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='checkb',
            field=models.CharField(default='张伟伟', max_length=32, verbose_name='充装工'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='checkc',
            field=models.CharField(default='王光春', max_length=32, verbose_name='充后检查员'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='factory',
            field=models.CharField(default='宣城百纳', max_length=32, verbose_name='制造厂商'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='fill_t',
            field=models.DateField(verbose_name='充装时间'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='fillweight',
            field=models.CharField(default='29.5kg', max_length=32, verbose_name='满瓶重量'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='gp_code',
            field=models.CharField(default='000000', max_length=32, verbose_name='钢瓶编号'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='jc_date',
            field=models.DateField(verbose_name='检测日期'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='sc_date',
            field=models.DateField(verbose_name='生产日期'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='weight',
            field=models.CharField(default='16kg', max_length=32, verbose_name='空瓶重量'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='zn_code',
            field=models.CharField(default='WR23-', max_length=32, verbose_name='站内编号'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='bf_date',
            field=models.DateField(verbose_name='报废日期'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='company',
            field=models.CharField(default='青山液化气站', max_length=100, verbose_name='充装单位'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='gp_code',
            field=models.CharField(default='000000', max_length=32, verbose_name='钢瓶编号'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='jc_date',
            field=models.DateField(verbose_name='检测日期'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='jf_code',
            field=models.CharField(default='000000', max_length=32, verbose_name='阀门编号'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='manufacturer',
            field=models.CharField(default='宣城市百纳压力容器制造有限公司', max_length=100, verbose_name='制造厂商'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='sc_date',
            field=models.DateField(verbose_name='生产日期'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='specification',
            field=models.CharField(default='YSP35.5', max_length=32, verbose_name='规格'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='xj_date',
            field=models.DateField(verbose_name='下次检测日期'),
        ),
        migrations.AlterField(
            model_name='gp',
            name='zn_code',
            field=models.CharField(default='WR23-', max_length=32, verbose_name='站内编号'),
        ),
        migrations.AlterField(
            model_name='record',
            name='address',
            field=models.CharField(default='陵阳镇', max_length=64, verbose_name='使用地址'),
        ),
        migrations.AlterField(
            model_name='record',
            name='client',
            field=models.CharField(max_length=64, verbose_name='客户名称'),
        ),
        migrations.AlterField(
            model_name='record',
            name='tel',
            field=models.CharField(max_length=32, verbose_name='预存电话'),
        ),
    ]
