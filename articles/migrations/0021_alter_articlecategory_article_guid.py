# Generated by Django 4.1.2 on 2022-11-01 00:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0020_articlelike_articles_articlelike_unique_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='article_guid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
    ]
