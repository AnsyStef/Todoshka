# Generated by Django 4.1 on 2022-11-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_notes_name_alter_notes_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, verbose_name='Логин')),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
            ],
        ),
    ]