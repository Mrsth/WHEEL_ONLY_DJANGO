# Generated by Django 3.2.7 on 2021-10-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=500)),
                ('blogContent', models.TextField()),
                ('blogOwner', models.CharField(max_length=100)),
                ('blogLink', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
