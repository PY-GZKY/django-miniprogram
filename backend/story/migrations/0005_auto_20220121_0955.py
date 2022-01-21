# Generated by Django 2.2.13 on 2022-01-21 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_auto_20220121_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='description',
            field=models.CharField(help_text='description', max_length=100),
        ),
        migrations.AlterField(
            model_name='stories',
            name='duration',
            field=models.TextField(help_text='duration'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='duration_raw',
            field=models.TextField(help_text='duration_raw'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='header',
            field=models.CharField(help_text='标题', max_length=100),
        ),
        migrations.AlterField(
            model_name='stories',
            name='image',
            field=models.ImageField(null=True, upload_to='book/%Y/%m', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='original_description',
            field=models.CharField(help_text='original_description', max_length=100),
        ),
        migrations.AlterField(
            model_name='stories',
            name='original_header',
            field=models.CharField(help_text='original_header', max_length=100),
        ),
        migrations.AlterField(
            model_name='stories',
            name='video',
            field=models.CharField(help_text='video', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicledetail',
            name='description',
            field=models.CharField(help_text='description', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicledetail',
            name='header',
            field=models.CharField(help_text='标题', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicledetail',
            name='image',
            field=models.ImageField(null=True, upload_to='book/%Y/%m', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='vehicledetail',
            name='vehicles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicles', to='story.Vehicles'),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='description',
            field=models.CharField(help_text='description', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='header',
            field=models.CharField(help_text='header', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='image',
            field=models.ImageField(null=True, upload_to='book/%Y/%m', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='sub_header',
            field=models.CharField(help_text='sub_header', max_length=100),
        ),
    ]
