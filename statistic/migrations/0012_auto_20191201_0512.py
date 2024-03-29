# Generated by Django 2.2.5 on 2019-12-01 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0011_auto_20191128_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statisticdata',
            name='netto',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=0, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='statisticdata',
            name='period',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='statisticdata',
            name='stoim',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=0, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='statisticdata',
            name='strana',
            field=models.CharField(blank=True, db_index=True, max_length=3, null=True),
        ),
    ]
