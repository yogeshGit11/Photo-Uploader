# Generated by Django 4.0.5 on 2022-07-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uppic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='imgs')),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
    ]
