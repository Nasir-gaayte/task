# Generated by Django 4.1.3 on 2022-12-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contactmodel_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imo', models.ImageField(upload_to='')),
                ('desc', models.TextField()),
            ],
        ),
    ]