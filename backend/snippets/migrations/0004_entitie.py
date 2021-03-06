# Generated by Django 3.1.8 on 2021-11-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20211119_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entitie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('header', models.CharField(blank=True, default='', max_length=100)),
                ('original_header', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=100)),
                ('original_description', models.CharField(blank=True, default='', max_length=100)),
                ('video', models.CharField(blank=True, default='', max_length=100)),
                ('image', models.CharField(blank=True, default='', max_length=100)),
                ('duration_raw', models.IntegerField()),
                ('duration', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'verbose_name': 'Entitie',
                'verbose_name_plural': 'Entitie',
            },
        ),
    ]
