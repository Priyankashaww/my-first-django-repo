# Generated by Django 4.1.5 on 2023-02-25 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_reserve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='date',
            field=models.CharField(max_length=255),
        ),
    ]
