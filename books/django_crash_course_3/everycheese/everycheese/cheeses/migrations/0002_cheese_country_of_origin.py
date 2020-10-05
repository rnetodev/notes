# Generated by Django 3.0.9 on 2020-08-28 18:00

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='country_of_origin',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Country of origin'),
        ),
    ]