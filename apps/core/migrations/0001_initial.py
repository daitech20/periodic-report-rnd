# Generated by Django 4.2.3 on 2023-07-08 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('fullname', models.CharField(max_length=30)),
                ('position', models.IntegerField(choices=[(0, 'SVCNTS'), (1, 'Dev 1'), (2, 'Dev 2'), (3, 'Dev 3')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
