# Generated by Django 4.1.2 on 2022-10-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0018_remove_articlelike_event_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentlike',
            name='event_type',
        ),
        migrations.AddField(
            model_name='commentlike',
            name='event_counter',
            field=models.IntegerField(default=1, verbose_name='Счетчик'),
        ),
    ]
