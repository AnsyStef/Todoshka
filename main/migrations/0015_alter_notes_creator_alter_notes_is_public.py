# Generated by Django 4.1.4 on 2023-01-01 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_notes_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='creator',
            field=models.CharField(default='System', max_length=15, verbose_name='Создатель'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Публично'),
        ),
    ]