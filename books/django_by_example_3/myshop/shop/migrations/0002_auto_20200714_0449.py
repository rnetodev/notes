# Generated by Django 3.0.8 on 2020-07-14 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='avaiable',
            new_name='available',
        ),
    ]
