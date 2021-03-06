# Generated by Django 2.2.6 on 2019-10-30 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_sharing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='car',
            name='end_use_date',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата завершения аренды автомобиля'),
        ),
        migrations.AlterField(
            model_name='car',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car_sharing.Order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='car',
            name='start_use_date',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата начала аренды автомобиля'),
        ),
    ]
