# Generated by Django 3.1.3 on 2021-06-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0018_auto_20210428_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
