# Generated by Django 3.0.3 on 2020-02-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeedetails', '0002_auto_20200219_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.PositiveIntegerField(max_length=10),
        ),
    ]
