# Generated by Django 4.2 on 2023-05-03 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_homeinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homeinfo',
            options={'ordering': ['-id']},
        ),
    ]
