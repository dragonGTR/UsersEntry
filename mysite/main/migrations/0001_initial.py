# Generated by Django 2.2.5 on 2021-06-28 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('DOB', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=20)),
                ('National', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Pin', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Qualification', models.CharField(max_length=100)),
                ('Salary', models.CharField(max_length=20)),
                ('PanNum', models.CharField(max_length=30)),
            ],
        ),
    ]
