# Generated by Django 3.2.4 on 2021-06-29 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_date_users_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
