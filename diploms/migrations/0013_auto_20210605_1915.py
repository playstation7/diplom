# Generated by Django 3.2.4 on 2021-06-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diploms', '0012_auto_20210605_1706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'cities'},
        ),
        migrations.AddField(
            model_name='vacansia',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]