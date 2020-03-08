# Generated by Django 2.1.7 on 2020-03-08 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custmanager', '0004_auto_20200307_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='custmanager.Tags'),
        ),
    ]