# Generated by Django 4.0.6 on 2023-01-31 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='school',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.CharField(default='', max_length=40, unique=True),
        ),
    ]
