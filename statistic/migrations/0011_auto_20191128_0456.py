# Generated by Django 2.2.5 on 2019-11-28 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0010_auto_20191127_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statisticdata',
            name='napr',
            field=models.CharField(blank=True, db_index=True, max_length=2, null=True),
        ),
    ]
