# Generated by Django 2.0.3 on 2018-05-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='name',
            field=models.CharField(default='no name', max_length=50),
        ),
    ]