# Generated by Django 4.1 on 2022-12-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_notes_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='creator',
            field=models.CharField(blank=True, max_length=15, verbose_name='Создатель'),
        ),
    ]
