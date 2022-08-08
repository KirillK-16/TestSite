# Generated by Django 3.2.7 on 2022-08-07 15:24

import catalog.models
import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20211130_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='cart_image',
            field=models.ImageField(blank=True, null=True, upload_to=catalog.models.get_file_path, validators=[catalog.validators.image_resolution_check_cart], verbose_name='Изображение для таблицы'),
        ),
    ]
