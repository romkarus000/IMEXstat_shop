# Generated by Django 2.2.5 on 2019-10-05 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_cabinet', '0004_auto_20191005_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='research',
            field=models.ManyToManyField(blank=True, null=True, to='products.Research'),
        ),
    ]
