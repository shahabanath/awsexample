# Generated by Django 3.1.3 on 2021-04-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0004_auto_20210422_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('mechanic', 'mechanic'), ('user', 'user')], max_length=11),
        ),
    ]