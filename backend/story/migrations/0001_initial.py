# Generated by Django 3.1.8 on 2022-01-20 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(help_text='header', max_length=100)),
                ('sub_header', models.CharField(help_text='sub_header', max_length=100)),
                ('description', models.CharField(help_text='description', max_length=300)),
                ('image', models.TextField(default='http://img4.youxiake.com/ps/2021/11/one/20eb546d5b21e3486b898feac1ee2b1a.jpg', help_text='image')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(help_text='文章标题', max_length=100)),
                ('original_header', models.CharField(help_text='文章标题', max_length=100)),
                ('description', models.CharField(help_text='文章标题', max_length=100)),
                ('original_description', models.CharField(help_text='文章标题', max_length=100)),
                ('video', models.CharField(help_text='文章标题', max_length=100)),
                ('image', models.TextField(help_text='文章正文')),
                ('duration_raw', models.TextField(help_text='文章正文')),
                ('duration', models.TextField(help_text='文章正文')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(help_text='文章标题', max_length=100)),
                ('sub_header', models.CharField(help_text='文章标题', max_length=100)),
                ('description', models.CharField(help_text='文章标题', max_length=100)),
                ('image', models.TextField(help_text='文章正文')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
