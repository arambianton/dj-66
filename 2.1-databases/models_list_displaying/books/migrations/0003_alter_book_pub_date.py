# Generated by Django 4.1.7 on 2023-03-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.CharField(max_length=20, verbose_name='Дата публикации'),
        ),
    ]
