# Generated by Django 3.1.3 on 2021-04-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_user_companyname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_approved',
            field=models.CharField(choices=[('approved', 'approved'), ('disapproved', 'disapproved')], default='disapproved', max_length=15),
        ),
    ]