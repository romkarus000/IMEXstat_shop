# Generated by Django 2.2.5 on 2019-10-30 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_cabinet', '0002_favorite_articles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='slug',
        ),
    ]
