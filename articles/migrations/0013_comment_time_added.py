# Generated by Django 4.1.2 on 2022-10-20 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_articlelike_date_added_commentlike_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time_added',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]