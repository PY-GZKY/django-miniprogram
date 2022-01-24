# Generated by Django 2.2.13 on 2022-01-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0017_auto_20220124_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storiedetail',
            name='description',
        ),
        migrations.AlterField(
            model_name='storiedetail',
            name='header',
            field=models.CharField(help_text='图片标题', max_length=100, verbose_name='图片标题'),
        ),
        migrations.AlterField(
            model_name='storiedetail',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d', verbose_name='图片'),
        ),
    ]
