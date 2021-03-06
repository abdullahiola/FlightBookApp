# Generated by Django 4.0.5 on 2022-06-22 00:17

import bookflightapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('airport_code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aeroplane', models.CharField(max_length=100)),
                ('departure_datetime', models.DateTimeField()),
                ('arrival_datetime', models.DateTimeField()),
                ('max_passengers', models.IntegerField()),
                ('price', models.IntegerField()),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='bookflightapp.airport')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='bookflightapp.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('reference_no', models.CharField(default=bookflightapp.models.random_string, editable=False, max_length=6, primary_key=True, serialize=False, unique=True)),
                ('passenger_first_name', models.CharField(max_length=200)),
                ('passenger_last_name', models.CharField(max_length=200)),
                ('booking_datetime', models.DateTimeField(auto_now_add=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflightapp.flight')),
            ],
        ),
    ]
