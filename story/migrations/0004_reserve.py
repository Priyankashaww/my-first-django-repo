# Generated by Django 4.1.5 on 2023-02-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_admins'),
    ]

    operations = [
        migrations.CreateModel(
            name='reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phno', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('seats', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'reserve',
            },
        ),
    ]
