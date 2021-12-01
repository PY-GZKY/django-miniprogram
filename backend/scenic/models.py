from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from markdown import Markdown


class Tag(models.Model):
    """景区标签"""
    text = models.CharField(max_length=30,help_text = '文章标签')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text


class Category(models.Model):
    """景区分类"""
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Avatar(models.Model):
    content = models.ImageField(upload_to='avatar/%Y%m%d')


class Article(models.Model):
    """景区文章 model"""
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='articles',
        help_text='文章作者'
    )
    # 分类
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='articles',
        help_text='文章分类'
    )
    # 标签
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='articles',
        verbose_name='文章标签',
        help_text='文章标签'
    )
    # 标题图
    avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='article',
        help_text='文章封面'
    )
    # 标题
    title = models.CharField(max_length=100, help_text='文章标题')
    # 正文
    body = models.TextField(help_text='文章正文')
    # 创建时间
    created = models.DateTimeField(default=timezone.now, help_text='创建时间')
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.body)
        return md_body, md.toc
