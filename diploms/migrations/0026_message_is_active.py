# Generated by Django 3.2.4 on 2021-06-07 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diploms', '0025_alter_message_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
