from django.db import models
from django.utils import timezone


class Slides(models.Model):
    """Slides model"""
    # header
    header = models.CharField(max_length=100, help_text='header')
    # sub_header
    sub_header = models.CharField(max_length=100, help_text='sub_header')
    # description
    description = models.CharField(max_length=300, help_text='description')
    # image
    image = models.ImageField(upload_to='book/%Y/%m', verbose_name='image', null=True)
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
    # 标题
    header = models.CharField(max_length=100, help_text='文章标题')
    # 标题
    sub_header = models.CharField(max_length=100, help_text='文章标题')
    # description
    description = models.CharField(max_length=100, help_text='文章标题')
    # image
    image = models.TextField(help_text='文章正文')
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
    vehicles = models.ForeignKey(Vehicles, on_delete=models.SET_NULL, null=True, blank=True, related_name="vehicles")
    # 标题
    header = models.CharField(max_length=100, help_text='文章标题')
    # description
    description = models.CharField(max_length=100, help_text='文章标题')
    # image
    image = models.TextField(help_text='文章正文')
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
    # 标题
    header = models.CharField(max_length=100, help_text='文章标题')
    # original_header
    original_header = models.CharField(max_length=100, help_text='文章标题')
    # description
    description = models.CharField(max_length=100, help_text='文章标题')
    # original_description
    original_description = models.CharField(max_length=100, help_text='文章标题')
    # video
    video = models.CharField(max_length=100, help_text='文章标题')
    # image
    image = models.TextField(help_text='文章正文')
    # duration_raw
    duration_raw = models.TextField(help_text='文章正文')
    # duration
    duration = models.TextField(help_text='文章正文')
    # 创建时间
    created = models.DateTimeField(default=timezone.now, help_text='创建时间')
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.header
