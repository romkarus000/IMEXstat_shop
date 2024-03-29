# Generated by Django 2.2.5 on 2019-12-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0012_auto_20191201_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticAggregateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(db_index=True)),
                ('imp_sum_cost', models.IntegerField(verbose_name='Импорт - суммарная стоимость')),
                ('exp_sum_cost', models.IntegerField(verbose_name='Экспорт - суммарная стоимость')),
                ('imp_sum_weight', models.IntegerField(verbose_name='Импорт - суммарный вес')),
                ('exp_sum_weight', models.IntegerField(verbose_name='Экспорт - суммарный вес')),
                ('imp_sum_unique_countries', models.IntegerField(verbose_name='Импорт - Количество вовлеченных стран')),
                ('exp_sum_unique_countries', models.IntegerField(verbose_name='Экспорт - Количество вовлеченных стран')),
                ('imp_tnved_by_max_cost', models.IntegerField(verbose_name='Импорт - Код тнвэд имеющий максимальную стоимость')),
                ('exp_tnved_by_max_cost', models.IntegerField(verbose_name='Экспорт - Код тнвэд имеющий максимальную стоимость')),
            ],
        ),
    ]
