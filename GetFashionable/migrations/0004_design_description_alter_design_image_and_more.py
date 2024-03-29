# Generated by Django 4.2.7 on 2024-02-15 16:26

import GetFashionable.models.Design
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetFashionable', '0003_design_image_height_design_image_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='image',
            field=models.ImageField(upload_to=GetFashionable.models.image_path),
        ),
        migrations.AlterField(
            model_name='design',
            name='image_height',
            field=models.PositiveIntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='design',
            name='image_width',
            field=models.PositiveIntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='design',
            name='name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
