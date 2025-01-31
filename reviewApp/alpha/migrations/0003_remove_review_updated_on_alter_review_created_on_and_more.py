# Generated by Django 4.1.7 on 2023-04-05 22:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0002_remove_product_timestamp_remove_review_timestamp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='updated_on',
        ),
        migrations.AlterField(
            model_name='review',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profile_pics'),
            preserve_default=False,
        ),
    ]
