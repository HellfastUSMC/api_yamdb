# Generated by Django 2.2.16 on 2022-02-18 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220217_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-slug']},
        ),
    ]
