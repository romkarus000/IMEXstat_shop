# Generated by Django 2.2.5 on 2019-10-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_cabinet', '0006_auto_20191005_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.IntegerField(blank=True, verbose_name='Мобильный телефон'),
        ),
    ]
