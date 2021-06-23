# Generated by Django 3.2.4 on 2021-06-23 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0012_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=100, null=True)),
                ('municipality', models.CharField(max_length=100, null=True)),
                ('barangay', models.CharField(max_length=100, null=True)),
                ('hs_num', models.CharField(max_length=100, null=True)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('card_number', models.CharField(max_length=100, null=True)),
                ('mm', models.CharField(max_length=2, null=True)),
                ('dd', models.CharField(max_length=2, null=True)),
                ('yyyy', models.CharField(max_length=4, null=True)),
                ('ccv', models.CharField(max_length=3, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_COD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=100, null=True)),
                ('municipality', models.CharField(max_length=100, null=True)),
                ('barangay', models.CharField(max_length=100, null=True)),
                ('hs_num', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]