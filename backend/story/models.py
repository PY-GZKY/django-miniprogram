from django.db import models
from django.forms import ModelForm, forms
from django.utils import timezone


class Slides(models.Model):
    """Slides model"""
    id = models.IntegerField(primary_key=True)
    # header
    header = models.CharField(max_length=100, help_text='header', verbose_name="标题")
    # sub_header
    sub_header = models.CharField(max_length=100, help_text='sub_header', verbose_name="子标题")
    # description
    description = models.CharField(max_length=300, help_text='description', verbose_name="简介")
    # image
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='图片', null=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now, help_text='创建时间', verbose_name="创建时间")
    # 更新时间
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        ordering = ['-created']
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.header


class Vehicles(models.Model):
    """Vehicles model"""
    id = models.IntegerField(primary_key=True, auto_created=True)
    # header
    header = models.CharField(max_length=100, help_text='header', verbose_name="标题")
    # sub_header
    sub_header = models.CharField(max_length=100, help_text='sub_header', verbose_name="子标题")
    # description
    description = models.CharField(max_length=100, help_text='description', verbose_name="简介")
    # image
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='图片', null=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now, help_text='创建时间', verbose_name="创建时间")
    # 更新时间
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        ordering = ['-created']
        verbose_name = '轶事列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.header


class VehicleDetail(models.Model):
    """VehicleDeatil model"""
    id = models.IntegerField(primary_key=True)
    vehicles = models.ForeignKey(Vehicles, on_delete=models.SET_NULL, null=True, blank=True, related_name="vehicles")
    # 标题
    header = models.CharField(max_length=100, help_text='标题', verbose_name="标题")
    # description
    description = models.CharField(max_length=100, help_text='description', verbose_name="简介")
    # image
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='图片', null=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now, help_text='创建时间', verbose_name="创建时间")
    # 更新时间
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        ordering = ['-created']
        verbose_name = '轶事详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.header

class Stories(models.Model):
    """Stories model"""
    id = models.IntegerField(primary_key=True)
    # 标题
    header = models.CharField(max_length=100, help_text='标题', verbose_name="标题")
    # description
    description = models.CharField(max_length=100, help_text='description', verbose_name="简介")
    # image
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='图片封面', null=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now, help_text='创建时间', verbose_name="创建时间")
    # 更新时间
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        ordering = ['-created']
        verbose_name = '故事列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.header

class StorieDetail(models.Model):
    """StorieDetail model"""
    id = models.IntegerField(primary_key=True)
    stories = models.ForeignKey(Stories, on_delete=models.SET_NULL, null=True, blank=True, related_name="stories", verbose_name="故事")
    # 标题
    header = models.CharField(max_length=100, help_text='图片标题', verbose_name="图片标题")
    # description
    # description = models.CharField(max_length=100, help_text='description', verbose_name="简介")
    # image
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='图片', null=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now, help_text='创建时间', verbose_name="创建时间")
    # 更新时间
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        ordering = ['-created']
        verbose_name = '故事详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.header




