# Generated by Django 4.1.7 on 2023-03-10 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
