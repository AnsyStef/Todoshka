# Generated by Django 4.1 on 2023-02-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_profile_trust_factor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.CharField(blank=True, default='Пользователь', max_length=13, null=True, verbose_name='Должность'),
        ),
    ]