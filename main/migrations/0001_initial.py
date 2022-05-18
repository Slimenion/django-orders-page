# Generated by Django 3.0.7 on 2022-05-15 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=255, verbose_name='Название программы')),
                ('price', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(max_length=255, verbose_name='Название услуги')),
                ('price', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customers_name', models.CharField(max_length=255, verbose_name='Имя заказчика')),
                ('email', models.EmailField(max_length=254)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Products')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Services')),
            ],
        ),
    ]
