# Generated by Django 4.1 on 2023-05-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='languages',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(max_length=300),
        ),
    ]