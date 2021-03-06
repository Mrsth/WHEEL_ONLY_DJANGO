# Generated by Django 3.2.7 on 2021-10-03 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bikeDisplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bikeUser', models.CharField(max_length=50)),
                ('bikeCompany', models.CharField(max_length=50)),
                ('bikeModel', models.CharField(max_length=50)),
                ('bikeNumber', models.CharField(max_length=50)),
                ('bikeColor', models.CharField(max_length=50)),
                ('bikeImage', models.ImageField(upload_to='')),
            ],
        ),
    ]
