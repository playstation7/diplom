# Generated by Django 3.2.4 on 2021-06-05 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diploms', '0010_remove_vacansia_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
    ]