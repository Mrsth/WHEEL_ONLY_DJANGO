# Generated by Django 3.2.7 on 2021-10-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_alter_blogmodel_blogcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='blogContent',
            field=models.TextField(),
        ),
    ]
