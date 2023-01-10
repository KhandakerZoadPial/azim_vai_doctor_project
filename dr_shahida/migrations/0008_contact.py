# Generated by Django 4.1.3 on 2023-01-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dr_shahida', '0007_rename_image_blogpost_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('subject', models.CharField(max_length=200, unique=True)),
                ('message', models.TextField(max_length=500, unique=True)),
            ],
        ),
    ]