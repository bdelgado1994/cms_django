# Generated by Django 4.2.3 on 2023-07-26 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'ordering': ['first_name']},
        ),
    ]
