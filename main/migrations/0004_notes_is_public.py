# Generated by Django 4.1 on 2022-11-09 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_notes_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
