# Generated by Django 2.2.5 on 2019-11-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0005_remove_statisticdata_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='statisticdata',
            name='datetime',
            field=models.DateField(blank=True, null=True),
        ),
    ]