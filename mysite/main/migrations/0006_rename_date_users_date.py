# Generated by Django 3.2.4 on 2021-06-29 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_users_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='date',
            new_name='Date',
        ),
    ]
