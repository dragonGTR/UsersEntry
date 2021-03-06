# Generated by Django 3.2.4 on 2021-06-29 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_users_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Response', models.CharField(max_length=100)),
                ('Reason', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='Responses',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.response'),
            preserve_default=False,
        ),
    ]
