from django.db import models

# Create your models here.
class Gp(models.Model):
    jf_code = models.CharField(max_length=32, default='000000', verbose_name='阀门编号')
    gp_code = models.CharField(max_length=32, default='000000', verbose_name='钢瓶编号')
    zn_code = models.CharField(max_length=32, default='WR23-', verbose_name='站内编号')
    sc_date = models.DateField(verbose_name='生产日期')
    jc_date = models.DateField(verbose_name='检测日期')
    manufacturer = models.CharField(max_length=100, default='宣城市百纳压力容器制造有限公司', verbose_name='制造厂商')
    specification = models.CharField(max_length=32, default='YSP35.5', verbose_name='规格')
    company = models.CharField(max_length=100, default='青山液化气站', verbose_name='充装单位')
    xj_date = models.DateField(verbose_name='下次检测日期')
    bf_date = models.DateField(verbose_name='报废日期')
    remark = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = '钢瓶表'
    # 给模型增加__str__()方法是很重要的，这不仅仅能给你在命令行里使用带来方便，Django自动生成的
    # admin里也使用这个方法来表示对象。
    def __str__(self):
        return self.gp_code


class Filling(models.Model):
    gp_code = models.CharField(max_length=32, default='000000', verbose_name='钢瓶编号')
    zn_code = models.CharField(max_length=32, default='WR23-', verbose_name='站内编号')
    factory = models.CharField(max_length=32, default='宣城百纳', verbose_name='制造厂商')
    sc_date = models.DateField(verbose_name='生产日期')
    jc_date = models.DateField(verbose_name='检测日期')
    weight = models.CharField(max_length=32, default='16kg', verbose_name='空瓶重量')
    checka = models.CharField(max_length=32, default='杜扬', verbose_name='充前检查员')
    fill_t = models.DateField(verbose_name='充装时间')
    process = models.CharField(max_length=32, default='正常')
    checkb = models.CharField(max_length=32, default='张伟伟', verbose_name='充装工')
    fillweight = models.CharField(max_length=32, default='29.5kg', verbose_name='满瓶重量')
    checkc = models.CharField(max_length=32, default='王光春', verbose_name='充后检查员')
    remark = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = '充装表'
    def __str__(self):
        return self.gp_code


class Record(models.Model):
    time = models.DateField('日期')
    gp_code = models.CharField(max_length=32, default='000000', verbose_name='钢瓶编号')
    client = models.CharField(max_length=64, verbose_name='客户名称')
    tel = models.CharField(max_length=32, verbose_name='预存电话')
    address = models.CharField(max_length=64, default='陵阳镇', verbose_name='使用地址')
    # DELIVERY_CHOICES = (
    #     ('1', '自取'),
    #     ('2', '杜扬'),
    #     (),
    #     (),
    # )
    # delivery = models.CharField(max_length=32, choices=DELIVERY_CHOICES, verbose_name='配送员')
    delivery = models.CharField(max_length=32, default='站点自取', verbose_name='配送员')
    remark = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = '收发记录表'
    def __str__(self):
        return self.gp_code
