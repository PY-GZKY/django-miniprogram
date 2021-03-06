# Generated by Django 2.2.6 on 2021-12-02 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scenic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(help_text='文章作者', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='avatar',
            field=models.ForeignKey(blank=True, help_text='文章封面', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to='scenic.Avatar'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(help_text='文章正文'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, help_text='文章分类', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='scenic.Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='文章标签', related_name='articles', to='scenic.Tag', verbose_name='文章标签'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text='文章标题', max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='text',
            field=models.CharField(help_text='文章标签', max_length=30),
        ),
    ]
