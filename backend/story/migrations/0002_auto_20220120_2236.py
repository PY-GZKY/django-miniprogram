# Generated by Django 3.1.8 on 2022-01-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slides',
            name='image',
            field=models.ImageField(null=True, upload_to='book', verbose_name='图片'),
        ),
    ]
