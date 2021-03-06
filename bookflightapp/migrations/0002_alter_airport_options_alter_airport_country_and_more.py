# Generated by Django 4.0.5 on 2022-06-30 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookflightapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airport',
            options={'ordering': ['name'], 'verbose_name_plural': 'Airports'},
        ),
        migrations.AlterField(
            model_name='airport',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
