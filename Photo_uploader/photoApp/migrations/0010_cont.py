# Generated by Django 4.0.5 on 2022-07-26 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoApp', '0009_uppic_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='cont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('mob', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
