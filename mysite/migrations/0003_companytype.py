# Generated by Django 4.0.6 on 2022-07-11 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_company_stockinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='其他', max_length=50, verbose_name='類別')),
            ],
        ),
    ]
