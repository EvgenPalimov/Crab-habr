# Generated by Django 4.1.2 on 2022-10-10 22:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_alter_userprofile_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='firstname',
            field=models.CharField(default='', max_length=128, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastname',
            field=models.CharField(default='', max_length=128, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_image',
            field=models.ImageField(blank=True, upload_to='users_avatar', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='creation_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=16, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='users_photo', verbose_name='Фотография'),
        ),
    ]
