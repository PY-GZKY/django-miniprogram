from django.db import models
from django.utils import timezone

from scenic.models import Article
from django.contrib.auth.models import User


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='评论者',
        help_text='评论者'
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        # verbose_name='评论文章',
        help_text='评论文章'

    )

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='children',
        verbose_name='父评论',
        help_text='父评论'
    )

    content = models.TextField(verbose_name='内容', help_text='评论内容')
    created = models.DateTimeField(default=timezone.now, verbose_name='时间', help_text='评论时间')

    class Meta:
        ordering = ['-created']
        verbose_name = '评论'
        # verbose_name_plural = verbose_name


    def __str__(self):
        return self.content[:20]
