# Generated by Django 2.1.7 on 2020-03-08 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custmanager', '0006_auto_20200307_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='custmanager.Tag'),
        ),
    ]