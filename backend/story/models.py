from django.db import models
from django.utils import timezone


class Slides(models.Model):
    """Slides model"""
    id = models.IntegerField(primary_key=True)
    # header
    header = models.CharField(max_length=100, help_text='header')
    # sub_header
    sub_header = models.CharField(max_length=100, help_text='sub_header')
    # description
    description = models.CharField(max_length=300, help_text='description')
    # image
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='image', null=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now, help_text='创建时间')
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.header


class Vehicles(models.Model):
    """Vehicles model"""
    id = models.IntegerField(primary_key=True, auto_created=True)
    # header
    header = models.CharField(max_length=100, help_text='header')
    # sub_header
    sub_header = models.CharField(max_length=100, help_text='sub_header')
    # description
    description = models.CharField(max_length=100, help_text='description')
    # image
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='image', null=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now, help_text='创建时间')
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.header


class VehicleDetail(models.Model):
    """VehicleDeatil model"""
    id = models.IntegerField(primary_key=True)
    vehicles = models.ForeignKey(Vehicles, on_delete=models.SET_NULL, null=True, blank=True, related_name="vehicles")
    # 标题
    header = models.CharField(max_length=100, help_text='标题')
    # description
    description = models.CharField(max_length=100, help_text='description')
    # image
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='image', null=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now, help_text='创建时间')
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.header


class Stories(models.Model):
    """Stories model"""
    id = models.IntegerField(primary_key=True)
    # 标题
    header = models.CharField(max_length=100, help_text='标题')
    # original_header
    original_header = models.CharField(max_length=100, help_text='original_header')
    # description
    description = models.CharField(max_length=100, help_text='description')
    # original_description
    original_description = models.CharField(max_length=100, help_text='original_description')
    # video
    video =  models.FileField(upload_to='video/%Y/%m/%d', null=True, blank=True, verbose_name="视频内容")
    # image
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='image', null=True)
    # duration_raw
    # duration_raw = models.TextField(help_text='duration_raw')
    # duration
    duration = models.TextField(help_text='duration')
    # 创建时间
    created = models.DateTimeField(default=timezone.now, help_text='创建时间')
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.header
