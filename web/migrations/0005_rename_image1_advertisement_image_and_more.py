# Generated by Django 4.0.2 on 2022-07-20 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_advertisement_delete_ad1_delete_ad2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='image1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='image2',
        ),
    ]
