# Generated by Django 2.2.5 on 2019-09-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]
