# Generated by Django 4.1 on 2022-11-03 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_notes_date_alter_notes_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name='Принято'),
        ),
    ]
