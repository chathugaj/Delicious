# Generated by Django 4.2.8 on 2024-01-05 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reservation.timeslot'),
        ),
    ]
