# Generated by Django 3.2.6 on 2023-01-30 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20230128_2153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ['-created_at'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
