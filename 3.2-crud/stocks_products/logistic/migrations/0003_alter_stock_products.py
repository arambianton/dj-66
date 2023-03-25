# Generated by Django 4.1.7 on 2023-03-20 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0002_alter_stock_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='stocks', through='logistic.StockProduct', to='logistic.product'),
        ),
    ]
