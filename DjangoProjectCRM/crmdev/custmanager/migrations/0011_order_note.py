# Generated by Django 2.1.7 on 2020-03-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custmanager', '0010_auto_20200308_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
