# Generated by Django 2.2.13 on 2022-01-24 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0014_auto_20220124_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='mp4',
            field=models.IntegerField(default=1, help_text='是否MP4', verbose_name='是否MP4'),
        ),
    ]
