# Generated by Django 2.2.3 on 2019-07-17 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='message',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
