# Generated by Django 3.1.3 on 2021-06-17 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0022_auto_20210616_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='vehicle_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]