# Generated by Django 2.2.5 on 2019-10-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20191020_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='short_description',
            field=models.TextField(max_length=134, verbose_name='Описание статьи'),
        ),
    ]
