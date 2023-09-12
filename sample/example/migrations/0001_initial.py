# Generated by Django 4.2.5 on 2023-09-12 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('D_ID', models.AutoField(primary_key=True, serialize=False)),
                ('D_NAME', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('E_ID', models.AutoField(primary_key=True, serialize=False)),
                ('E_NAME', models.CharField(max_length=100)),
                ('DEPARTMENT', models.CharField(max_length=100)),
                ('DATE_OF_JOINING', models.DateField()),
                ('PHOTOFILENAME', models.CharField(max_length=100)),
            ],
        ),
    ]
