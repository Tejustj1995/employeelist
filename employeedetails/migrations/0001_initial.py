# Generated by Django 3.0.3 on 2020-02-19 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('empcode', models.CharField(max_length=30)),
                ('mobile', models.IntegerField(max_length=10)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeedetails.Position')),
            ],
        ),
    ]