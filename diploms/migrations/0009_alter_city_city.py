# Generated by Django 3.2.4 on 2021-06-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diploms', '0008_vacansia_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(default='Москва', max_length=100),
        ),
    ]