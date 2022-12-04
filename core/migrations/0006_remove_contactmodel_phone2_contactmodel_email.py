# Generated by Django 4.1.3 on 2022-12-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_contactmodel_phone2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='phone2',
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
