# Generated by Django 4.0.2 on 2022-02-02 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0002_auto_20220202_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decade',
            name='start_year',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='fad',
            name='description',
            field=models.CharField(default='no description', max_length=500),
        ),
        migrations.AlterField(
            model_name='fad',
            name='image_url',
            field=models.CharField(default='no image URL', max_length=500),
        ),
        migrations.AlterField(
            model_name='fad',
            name='name',
            field=models.CharField(default='no name', max_length=500),
        ),
    ]
