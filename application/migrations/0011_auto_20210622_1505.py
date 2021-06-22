# Generated by Django 3.2.3 on 2021-06-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_accessories_smartphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='carousel_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='carousel_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='carousel_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='accessories',
            name='brand',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
