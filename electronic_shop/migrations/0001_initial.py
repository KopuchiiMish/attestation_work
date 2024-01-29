# Generated by Django 5.0.1 on 2024-01-29 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('model', models.CharField(max_length=100, verbose_name='Модель продукта')),
                ('release_date', models.DateField(verbose_name='Дата выпуска на рынок')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='TradingNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название торговой сети')),
            ],
            options={
                'verbose_name': 'Торговая сеть',
                'verbose_name_plural': 'Торговые сети',
            },
        ),
        migrations.CreateModel(
            name='NetworkUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(
                    choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], default=0,
                    verbose_name='Тип поставщика')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название поставщика')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True,
                                            verbose_name='Email поставщика')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('debt_to_supplier',
                 models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True,
                                     verbose_name='Задолженность перед поставщиком')),
                ('products', models.ManyToManyField(to='electronic_shop.product', verbose_name='Продукты')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                               to='electronic_shop.networkunit', verbose_name='Подрядчик')),
                ('trading_network',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic_shop.tradingnetwork',
                                   verbose_name='Торговая сеть')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
    ]