# Generated by Django 3.1.3 on 2021-04-25 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0009_remove_insurance_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance',
            name='status',
            field=models.CharField(choices=[('requested', 'requested'), ('renewed', 'renewed')], default='', max_length=15),
        ),
    ]
