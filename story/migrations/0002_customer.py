# Generated by Django 4.1.5 on 2023-02-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('pwd', models.CharField(max_length=50)),
                ('phno', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=10)),
                ('psd', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]