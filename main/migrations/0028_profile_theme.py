# Generated by Django 4.1 on 2023-03-31 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_notes_status_alter_notes_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='theme',
            field=models.CharField(default='forest', max_length=20, verbose_name='Тема'),
        ),
    ]
