# Generated by Django 4.0.2 on 2022-02-01 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0002_auto_20220201_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decade',
            name='start_year',
            field=models.CharField(max_length=100),
        ),
    ]
