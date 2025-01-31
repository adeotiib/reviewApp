# Generated by Django 4.1.7 on 2023-04-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0013_product_timestamp_alter_product_date_released'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='timestamp',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_released',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='timestamp',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_on',
            field=models.DateField(blank=True),
        ),
    ]
