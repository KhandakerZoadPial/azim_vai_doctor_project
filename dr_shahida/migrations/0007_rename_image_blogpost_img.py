# Generated by Django 4.1.3 on 2022-12-27 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dr_shahida', '0006_alter_blogpost_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='image',
            new_name='img',
        ),
    ]
