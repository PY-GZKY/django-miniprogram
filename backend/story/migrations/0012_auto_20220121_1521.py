# Generated by Django 2.2.13 on 2022-01-21 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0011_auto_20220121_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slides',
            name='created',
            field=models.DateTimeField(default='2022-01-21 15:21:43', help_text='创建时间'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='created',
            field=models.DateTimeField(default='2022-01-21 15:21:43', help_text='创建时间'),
        ),
        migrations.AlterField(
            model_name='vehicledetail',
            name='created',
            field=models.DateTimeField(default='2022-01-21 15:21:43', help_text='创建时间'),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='created',
            field=models.DateTimeField(default='2022-01-21 15:21:43', help_text='创建时间'),
        ),
    ]
