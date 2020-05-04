# Generated by Django 2.2.11 on 2020-05-04 15:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filename_database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarcodeNode',
            fields=[
                ('barcode', models.IntegerField(primary_key=True, serialize=False)),
                ('valid_cache', models.BooleanField(default=False)),
                ('image', models.BinaryField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChargeCycleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.IntegerField()),
                ('constant_rate', models.FloatField()),
                ('end_rate', models.FloatField()),
                ('end_rate_prev', models.FloatField()),
                ('end_voltage', models.FloatField()),
                ('end_voltage_prev', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle_number', models.IntegerField()),
                ('valid_cycle', models.BooleanField(default=True)),
                ('processed', models.BooleanField(default=False)),
                ('chg_total_capacity', models.FloatField(null=True)),
                ('chg_average_voltage', models.FloatField(null=True)),
                ('chg_minimum_voltage', models.FloatField(null=True)),
                ('chg_maximum_voltage', models.FloatField(null=True)),
                ('chg_average_current_by_capacity', models.FloatField(null=True)),
                ('chg_average_current_by_voltage', models.FloatField(null=True)),
                ('chg_minimum_current', models.FloatField(null=True)),
                ('chg_maximum_current', models.FloatField(null=True)),
                ('chg_duration', models.FloatField(null=True)),
                ('dchg_total_capacity', models.FloatField(null=True)),
                ('dchg_average_voltage', models.FloatField(null=True)),
                ('dchg_minimum_voltage', models.FloatField(null=True)),
                ('dchg_maximum_voltage', models.FloatField(null=True)),
                ('dchg_average_current_by_capacity', models.FloatField(null=True)),
                ('dchg_average_current_by_voltage', models.FloatField(null=True)),
                ('dchg_minimum_current', models.FloatField(null=True)),
                ('dchg_maximum_current', models.FloatField(null=True)),
                ('dchg_duration', models.FloatField(null=True)),
                ('charge_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cycling.ChargeCycleGroup')),
            ],
        ),
        migrations.CreateModel(
            name='DischargeCycleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.IntegerField()),
                ('constant_rate', models.FloatField()),
                ('end_rate', models.FloatField()),
                ('end_rate_prev', models.FloatField()),
                ('end_voltage', models.FloatField()),
                ('end_voltage_prev', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.IntegerField()),
                ('step_type', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField()),
                ('second_accuracy', models.BooleanField()),
                ('total_capacity', models.FloatField(null=True)),
                ('average_voltage', models.FloatField(null=True)),
                ('minimum_voltage', models.FloatField(null=True)),
                ('maximum_voltage', models.FloatField(null=True)),
                ('average_current_by_capacity', models.FloatField(null=True)),
                ('average_current_by_voltage', models.FloatField(null=True)),
                ('minimum_current', models.FloatField(null=True)),
                ('maximum_current', models.FloatField(null=True)),
                ('duration', models.FloatField(null=True)),
                ('constant_voltage', models.FloatField(null=True)),
                ('end_voltage', models.FloatField(null=True)),
                ('end_voltage_prev', models.FloatField(null=True)),
                ('constant_current', models.FloatField(null=True)),
                ('end_current', models.FloatField(null=True)),
                ('end_current_prev', models.FloatField(null=True)),
                ('v_c_q_t_data', models.BinaryField(null=True)),
                ('cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cycling.Cycle')),
            ],
        ),
        migrations.CreateModel(
            name='CyclingFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_time', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('process_time', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('database_file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='filename_database.DatabaseFile')),
            ],
        ),
        migrations.AddField(
            model_name='cycle',
            name='cycling_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cycling.CyclingFile'),
        ),
        migrations.AddField(
            model_name='cycle',
            name='discharge_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cycling.DischargeCycleGroup'),
        ),
    ]