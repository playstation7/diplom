# Generated by Django 3.2.4 on 2021-06-05 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diploms', '0019_auto_20210606_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview',
            old_name='candidat',
            new_name='сandidate',
        ),
    ]
