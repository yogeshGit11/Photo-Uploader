# Generated by Django 4.0.5 on 2022-07-25 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoApp', '0008_remove_uppic_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='uppic',
            name='pic',
            field=models.ImageField(blank=True, upload_to='imgs'),
        ),
    ]
