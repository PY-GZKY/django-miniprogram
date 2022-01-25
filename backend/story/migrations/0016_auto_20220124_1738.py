# Generated by Django 2.2.13 on 2022-01-24 09:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0015_stories_mp4'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorieDetail',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('header', models.CharField(help_text='标题', max_length=100, verbose_name='标题')),
                ('description', models.CharField(help_text='description', max_length=100, verbose_name='简介')),
                ('image', models.ImageField(null=True, upload_to='images/%Y/%m/%d', verbose_name='图片封面')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '故事详情',
                'verbose_name_plural': '故事详情',
                'ordering': ['-created'],
            },
        ),
        migrations.RemoveField(
            model_name='stories',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='mp4',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='original_description',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='original_header',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='video',
        ),
        migrations.AddField(
            model_name='stories',
            name='images',
            field=models.ManyToManyField(related_name='images', to='story.StorieDetail', verbose_name='图片合集'),
        ),
    ]