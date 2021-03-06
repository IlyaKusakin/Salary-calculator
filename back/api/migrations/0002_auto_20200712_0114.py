# Generated by Django 3.0.7 on 2020-07-11 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='company',
            field=models.CharField(blank=True, max_length=150, verbose_name='Название  компании'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='skills',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Ключевые навыки'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='text',
            field=models.CharField(blank=True, max_length=5000, verbose_name='Подробное описание'),
        ),
    ]
