# Generated by Django 3.2.4 on 2021-06-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diploms', '0016_alter_vacansia_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacansia',
            name='image',
            field=models.ImageField(blank=True, default='media/noimage.jpg', null=True, upload_to='media/'),
        ),
    ]
