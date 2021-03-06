# Generated by Django 3.2.7 on 2021-10-10 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardApp', '0013_alter_bikedisplay_bikenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikedisplay',
            name='bikeCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardApp.bikecompanymodel'),
        ),
        migrations.AlterField(
            model_name='bikedisplay',
            name='bikeModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardApp.userbikemodel'),
        ),
    ]
