# Generated by Django 4.1.4 on 2023-01-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_notes_creator_alter_notes_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=15, verbose_name='Название группы')),
                ('group_password', models.CharField(blank=True, max_length=30, verbose_name='Пароль группы')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.CharField(blank=True, max_length=15, verbose_name='Группа пользователя'),
        ),
    ]