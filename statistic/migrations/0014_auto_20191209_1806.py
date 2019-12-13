# Generated by Django 2.2.5 on 2019-12-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0013_statisticaggregatedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statisticaggregatedata',
            name='exp_sum_cost',
            field=models.BigIntegerField(verbose_name='Экспорт - суммарная стоимость'),
        ),
        migrations.AlterField(
            model_name='statisticaggregatedata',
            name='exp_sum_unique_countries',
            field=models.BigIntegerField(verbose_name='Экспорт - Количество вовлеченных стран'),
        ),
        migrations.AlterField(
            model_name='statisticaggregatedata',
            name='exp_sum_weight',
            field=models.BigIntegerField(verbose_name='Экспорт - суммарный вес'),
        ),
        migrations.AlterField(
            model_name='statisticaggregatedata',
            name='exp_tnved_by_max_cost',
            field=models.BigIntegerField(verbose_name='Экспорт - Код тнвэд имеющий максимальную стоимость'),
        ),
        migrations.AlterField(
            model_name='statisticaggregatedata',
            name='imp_sum_cost',
            field=models.BigIntegerField(verbose_name='Импорт - суммарная стоимость'),
        ),
        migrations.AlterField(
            model_name='statisticaggregatedata',
            name='imp_sum_unique_countries',
            field=models.BigIntegerField(verbose_name='Импорт - Количество вовлеченных стран'),
        ),
        migrations.AlterField(
            model_name='statisticaggregatedata',
            name='imp_sum_weight',
            field=models.BigIntegerField(verbose_name='Импорт - суммарный вес'),
        ),
        migrations.AlterField(
            model_name='statisticaggregatedata',
            name='imp_tnved_by_max_cost',
            field=models.BigIntegerField(verbose_name='Импорт - Код тнвэд имеющий максимальную стоимость'),
        ),
    ]
