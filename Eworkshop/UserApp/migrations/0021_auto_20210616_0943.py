# Generated by Django 3.1.3 on 2021-06-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0020_auto_20210616_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
