# Generated by Django 3.1.3 on 2021-04-24 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0008_insurance_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurance',
            name='phone',
        ),
    ]
