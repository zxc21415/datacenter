# Generated by Django 4.0.6 on 2022-07-08 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='編碼')),
                ('name', models.CharField(max_length=20, verbose_name='名稱')),
            ],
        ),
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateinfo', models.DateField(verbose_name='日期')),
                ('open_price', models.FloatField(verbose_name='開盤價')),
                ('close_price', models.FloatField(verbose_name='收盤價')),
                ('volume', models.PositiveIntegerField(verbose_name='數量')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.company', verbose_name='公司名稱')),
            ],
        ),
    ]
